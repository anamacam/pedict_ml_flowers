# train.py

# Importar las librerías necesarias
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Función principal para entrenar el modelo
def train_model():
    # Cargar los datos
    data = pd.read_csv('data/dataset.csv')
    
    # Preprocesamiento de los datos
    X = data.drop('target', axis=1)
    y = data['target']
    
    # Dividir los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Inicializar el modelo
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    
    # Entrenar el modelo
    model.fit(X_train, y_train)
    
    # Evaluar el modelo
    accuracy = model.score(X_test, y_test)
    print(f'Accuracy: {accuracy}')

if __name__ == "__main__":
    train_model() 