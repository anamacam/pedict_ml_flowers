# utils.py

# Aquí puedes añadir funciones auxiliares que se usen en el proyecto

def save_experiment_results(results, filename='experiment_results.txt'):
    """Guarda los resultados de un experimento en un archivo de texto."""
    with open(f'experiments/{filename}', 'w') as file:
        for key, value in results.items():
            file.write(f'{key}: {value}\n') 