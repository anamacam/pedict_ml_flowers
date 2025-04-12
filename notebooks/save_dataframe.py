import pandas as pd
import os
import sys

# Obtener la ruta del directorio actual
current_dir = os.path.dirname(os.path.abspath(__file__))
# Obtener la ruta del directorio del proyecto (un nivel arriba)
project_dir = os.path.dirname(current_dir)
# Añadir la ruta del proyecto al sys.path para poder importar módulos del proyecto
sys.path.append(project_dir)

# Verificar si existe la carpeta processed, si no, crearla
processed_dir = os.path.join(project_dir, 'data', 'processed')
if not os.path.exists(processed_dir):
    os.makedirs(processed_dir)

def save_dataframe(df, filename='merged_data.csv'):
    """
    Guarda un dataframe en la carpeta de datos procesados.
    
    Args:
        df: El dataframe a guardar
        filename: Nombre del archivo CSV (por defecto 'merged_data.csv')
    """
    output_path = os.path.join(processed_dir, filename)
    df.to_csv(output_path, index=False)
    print(f"DataFrame guardado exitosamente en: {output_path}")
    return output_path

# Si este script se ejecuta directamente, intenta guardar df_merged desde el entorno
if __name__ == "__main__":
    # Este código se ejecutará si el script se llama directamente
    try:
        # Intenta obtener df_merged del entorno global
        from IPython import get_ipython
        ipython = get_ipython()
        
        if ipython is not None:
            # Si estamos en un entorno de IPython/Jupyter
            if 'df_merged' in ipython.user_ns:
                df_to_save = ipython.user_ns['df_merged']
                save_dataframe(df_to_save)
            else:
                print("Error: No se encontró 'df_merged' en el entorno actual.")
        else:
            print("Este script debe ejecutarse desde un notebook de Jupyter.")
    except ImportError:
        print("Este script debe ejecutarse desde un notebook de Jupyter.")
    except Exception as e:
        print(f"Error al guardar el dataframe: {str(e)}") 