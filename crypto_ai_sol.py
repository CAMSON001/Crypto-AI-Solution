import hashlib
import time
import os
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES, PKCS1_OAEP
import hmac


#Import the model and loading in our package 
from ml_crypto import load_and_train_model


# --- Génération des clés RSA pour le chiffrement hybride ---
def generate_rsa_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

# --- Génération dynamique de la clé AES avec renforcement ---
def generate_dynamic_aes_key(prediction):
    if prediction == 1:  # Si une attaque est détectée
        print("cle renforcee car attack detectee")
        entropy = get_random_bytes(32)
        return hashlib.sha512(entropy + b'attack').digest()[:32]  # Clé renforcée AES-256
    else:
        print("Pas d'attack, cle avec taille minimal")
        entropy = get_random_bytes(16)
        return hashlib.sha256(entropy + b'benign').digest()[:32]  # Clé standard AES-128

# --- Chiffrement AES avec authentification HMAC ---
def encrypt_data(data, aes_key, rsa_public_key):
    # Chiffrement AES
    cipher_aes = AES.new(aes_key, AES.MODE_CBC)
    ciphertext = cipher_aes.encrypt(pad(data.encode(), AES.block_size))
    
    # HMAC pour authentification
    hmac_digest = hmac.new(aes_key, ciphertext, hashlib.sha256).digest()
    
    # Chiffrement de la clé AES avec RSA
    rsa_key = RSA.import_key(rsa_public_key)
    cipher_rsa = PKCS1_OAEP.new(rsa_key)
    encrypted_aes_key = cipher_rsa.encrypt(aes_key)
    
    return encrypted_aes_key + cipher_aes.iv + hmac_digest + ciphertext

# --- Déchiffrement des données ---
def decrypt_data(encrypted_data, rsa_private_key):
    rsa_key = RSA.import_key(rsa_private_key)
    cipher_rsa = PKCS1_OAEP.new(rsa_key)
    
    # Extraction des segments
    encrypted_aes_key = encrypted_data[:256]
    iv = encrypted_data[256:272]
    hmac_digest = encrypted_data[272:304]
    ciphertext = encrypted_data[304:]
    
    # Déchiffrement de la clé AES
    aes_key = cipher_rsa.decrypt(encrypted_aes_key)
    
    # Vérification HMAC
    if hmac.new(aes_key, ciphertext, hashlib.sha256).digest() != hmac_digest:
        raise ValueError("Données corrompues ou altérées.")
    
    # Déchiffrement AES
    cipher_aes = AES.new(aes_key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher_aes.decrypt(ciphertext), AES.block_size)
    return decrypted_data.decode()

# --- Fonction de prédiction avec le modèle SVM ---

def predict_attack(packet, model):
    """Prédiction du modèle pour savoir si un paquet est benign ou une attaque."""
    prediction = model.predict([packet])
    return prediction[0]  # Retourne la prédiction (0 = benign, 1 = attaque)

# --- Intégration : Prédiction et chiffrement/déchiffrement ---

def main():
    # Charger le modèle et les données de test
    svm_model, X_test = load_and_train_model()
    # Générer les clés RSA
    private_key, public_key = generate_rsa_keys()
    # Prendre un exemple de paquet de test
    for i in range(10,20,2):
    
        packet_example = X_test[i]# Par exemple, on prend le premier paquet de X_test

       # Prédire si le paquet est benign ou une attaque
        prediction = predict_attack(packet_example, svm_model)

        # Génération de la clé AES
        aes_key = generate_dynamic_aes_key(prediction)
        
        # Données à chiffrer
        data = "Données sensibles à protéger"
        encrypted_data = encrypt_data(data, aes_key, public_key)
        decrypted_data = decrypt_data(encrypted_data, private_key)
        
        print("Données chiffrées:", encrypted_data)
        print("Données déchiffrées:", decrypted_data)

if __name__ == "__main__":
    main()