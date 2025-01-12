#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.model_selection import train_test_split


    # Charger les données
def load_and_train_model():    
    df = pd.read_csv("dataset_fi.csv")
    df = df.head(6702)


   

    X = df.drop('Label', axis=1)
    # Créer un encodeur pour les labels
    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(df['Label'])


    # Scaled X to choose features

    # Standardisation des features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X_scaled = X_scaled - X_scaled.min() 

    X_scaled


    # Select the 10 best features

    # Appliquer le test chi2 pour la sélection des meilleures features
    k = 10  # Choisir le nombre de features à garder
    chi2_selector = SelectKBest(chi2, k=k)
    X_new = chi2_selector.fit_transform(X_scaled, y)
    # Afficher les features sélectionnées
    selected_features = X.columns[chi2_selector.get_support(indices=True)]
    print("Les meilleures features sélectionnées : ", selected_features)



    # Liste des colonnes que vous voulez récupérer
    columns_to_select = ['Protocol', 'Fwd Packet Length Min', 'Fwd Packet Length Mean',
                        'Flow Packets/s', 'Fwd Packets/s', 'Packet Length Min',
                        'Packet Length Mean', 'Down/Up Ratio', 'Avg Packet Size',
                        'Avg Fwd Segment Size']

    # Sélectionner les colonnes dans votre DataFrame
    X_selected = df[columns_to_select]
    X_selected



    # Diviser les données en ensembles d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(X_selected, y, test_size=0.2, random_state=42)

    # Normalisation des données
    scaler_n = StandardScaler()
    X_train = scaler_n.fit_transform(X_train)
    X_test = scaler_n.transform(X_test)



    # Entraîner le modèle SVM
    svm_model = SVC(kernel='rbf', C=1.0, gamma='scale')
    svm_model.fit(X_train, y_train)


    # Prédictions
    y_pred = svm_model.predict(X_test)

    # Évaluation du modèle
    #rint("Matrice de confusion:\n", confusion_matrix(y_test, y_pred))
   #print("\nRapport de classification:\n", classification_report(y_test, y_pred))

    return svm_model, X_test 


#svm_model, X_test = load_and_train_model()
#print(X_test)