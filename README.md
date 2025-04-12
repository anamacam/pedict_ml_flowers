# Predict ML Flowers

Este proyecto tiene como objetivo predecir información relacionada con flores utilizando técnicas de Machine Learning.

## Estructura del Proyecto

```
.
├── .git/                  # Directorio de Git
├── .gitignore             # Archivos ignorados por Git
├── data/
│   ├── processed/         # Datos procesados
│   │   └── merged_data.csv
│   ├── raw/               # Datos crudos (mover aquí flor_2021_2024.xlsx y Summary.csv)
│   └── flor_2021_2024.xlsx  # (Mover a data/raw)
│   └── Summary.csv          # (Mover a data/raw)
├── experiments/           # Directorio para guardar experimentos (vacío por ahora)
├── models/                # Directorio para guardar modelos entrenados (vacío por ahora)
├── notebooks/
│   ├── Data_Preprocessing.ipynb # Notebook para preprocesamiento de datos
│   └── save_dataframe.py    # Script auxiliar para guardar DataFrames
├── src/
│   ├── __init__.py
│   ├── train.py           # Script de entrenamiento (esqueleto)
│   └── utils.py           # Funciones de utilidad (esqueleto)
├── venv/                  # Ambiente virtual (ignorado por Git)
└── README.md              # Este archivo
```

## Pasos Realizados

1.  **Configuración Inicial:** Creación de la estructura de carpetas y el ambiente virtual.
2.  **Preprocesamiento de Datos:** Carga, limpieza, unión y guardado de los datos iniciales (ver `notebooks/Data_Preprocessing.ipynb`).
3.  **Control de Versiones:** Inicialización de Git y subida del proyecto a GitHub.

## Próximos Pasos

-   Análisis Exploratorio de Datos (EDA).
-   Ingeniería de Características (Feature Engineering).
-   Entrenamiento del modelo de Machine Learning.
-   Evaluación del modelo. 