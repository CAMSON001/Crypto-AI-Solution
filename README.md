# Crypto-AI-Solution

## Description

**Crypto-AI-Solution** est un projet innovant qui intègre l'intelligence artificielle et la cryptographie avancée pour protéger les données sensibles dans un environnement réseau. Le système utilise un modèle d'apprentissage supervisé basé sur un SVM (Support Vector Machine) pour classer les paquets réseau en tant que **bénins** ou **attaques**. En fonction de la prédiction, le système génère dynamiquement une clé AES renforcée (si une attaque est détectée) ou une clé AES standard (si aucun problème n'est détecté). Les données sont ensuite chiffrées avec AES et protégées par un mécanisme d'authentification HMAC. La clé AES est chiffrée avec RSA pour assurer la sécurité de la clé elle-même.

Ce projet illustre comment utiliser l'IA pour améliorer la sécurité des systèmes en temps réel, tout en appliquant des pratiques de chiffrement avancées.

## Fonctionnalités

- **Détection d'attaques réseau** : Utilisation d'un modèle d'apprentissage supervisé (SVM) pour prédire si un paquet réseau est bénin ou une attaque.
- **Chiffrement hybride** : Le projet applique une méthode de chiffrement hybride en combinant RSA et AES.
  - **RSA** est utilisé pour chiffrer la clé AES.
  - **AES** chiffre les données sensibles.
- **Renforcement dynamique des clés AES** : La clé AES est générée dynamiquement en fonction de la prédiction du modèle SVM. Une clé AES renforcée est générée pour les attaques détectées et une clé AES standard est utilisée pour les paquets bénins.
- **Authentification HMAC** : Utilisation de HMAC pour garantir l'intégrité des données chiffrées.
- **Prédiction en temps réel** : Prédiction de la nature des paquets réseau et adaptation du chiffrement en fonction du résultat.

## Technologies Utilisées

- **Python** : Langage de programmation principal.
- **Scikit-learn** : Utilisé pour le modèle de machine learning (SVM) et la sélection des meilleures caractéristiques.
- **PyCryptodome** : Bibliothèque pour les opérations cryptographiques (RSA, AES, HMAC).
- **Pandas** : Manipulation et prétraitement des données.
- **Hashlib** : Fonctionnalités de hachage pour renforcer la sécurité.

## Prérequis

Pour faire fonctionner ce projet sur votre machine, vous devez installer les bibliothèques suivantes :

```bash
pip install pandas scikit-learn pycryptodome


Fichiers du Projet
ml_crypto.py : Ce fichier contient la logique pour charger le jeu de données, entraîner un modèle SVM, et sélectionner les meilleures fonctionnalités du dataset pour l'entraînement.
crypto_ai_sol.py : Ce fichier intègre la détection d'attaques réseau avec le chiffrement et déchiffrement des données, ainsi que la gestion des clés RSA et AES.

Structure du Projet
bash
Copy code
Crypto-AI-Solution/
│
├── ml_crypto.py            # Entraînement du modèle SVM et sélection des features
├── crypto_ai_sol.py        # Prédiction des attaques et chiffrement/déchiffrement des données
├── dataset_fi.csv          # Jeu de données de paquets réseau (utilisé pour l'entraînement du modèle)
├── README.md               # Ce fichier
└── LICENSE                 # Fichier de licence

Comment Exécuter le Projet
1. Entraînement du modèle
Avant d'utiliser le chiffrement, vous devez entraîner le modèle SVM avec le fichier ml_crypto.py. Ce modèle sert à prédire si un paquet réseau est bénin ou une attaque.

bash
Copy code
python ml_crypto.py

Cela entraînera le modèle en utilisant les données disponibles dans dataset_fi.csv et sélectionnera les meilleures fonctionnalités pour l'entraînement.

2. Exécution de la solution cryptographique
Après avoir entraîné le modèle, vous pouvez exécuter crypto_ai_sol.py pour tester la solution de chiffrement et déchiffrement basée sur les prédictions du modèle.

bash
Copy code
python crypto_ai_sol.py

Ce script prendra un échantillon des paquets dans X_test, effectuera une prédiction (attaque ou bénin), générera la clé AES en fonction de la prédiction et procédera au chiffrement des données. Il affichera ensuite les données chiffrées et déchiffrées.

Exemple de Sortie
python
Copy code
Prédiction: Attaque détectée
Clé AES générée: 32 bytes
Données sensibles chiffrées: b'...'
Données déchiffrées: Données sensibles à protéger

Prédiction: Pas d'attaque
Clé AES générée: 16 bytes
Données sensibles chiffrées: b'...'
Données déchiffrées: Données sensibles à protéger


Contribuer
Les contributions sont les bienvenues ! Si vous souhaitez améliorer le projet ou ajouter des fonctionnalités, veuillez suivre ces étapes :

Forkez ce projet.
Créez une branche pour votre fonctionnalité (git checkout -b feature/ma-fonctionnalité).
Faites vos modifications et validez-les (git commit -am 'Ajout de fonctionnalité').
Poussez votre branche (git push origin feature/ma-fonctionnalité).
Créez une Pull Request.
License
Ce projet est sous la licence MIT. Voir le fichier LICENSE pour plus de détails.

Merci d'avoir consulté Crypto-AI-Solution. Nous espérons que vous apprécierez le projet et que vous y trouverez une manière novatrice d'intégrer l'intelligence artificielle et la cryptographie pour renforcer la sécurité des systèmes.

rust
Copy code

Ce fichier `README.md` est conçu pour donner aux utilisateurs un aperçu complet de votre projet, comment l'exécuter, et comment y contribuer. Il décrit de manière détaillée les fonctionnalités du projet, la structure des fichiers, ainsi que les étapes nécessaires pour commencer à utiliser la solution.






