import pandas as pd
import os

# Ruta al directorio que contiene los archivos Excel
directorio_excel = './'

# Ruta al directorio donde se guardarán los archivos CSV
directorio_csv = './csvFromExcel'

# Crear el directorio CSV si no existe
if not os.path.exists(directorio_csv):
    os.makedirs(directorio_csv)

# Obtener la lista de archivos Excel en el directorio
archivos_excel = [archivo for archivo in os.listdir(directorio_excel) if archivo.endswith('.xlsx') and not archivo.startswith('~$')]

# Iterar sobre cada archivo Excel
for archivo_excel in archivos_excel:
    # Leer el archivo Excel
    print("Procesando ", archivo_excel)
    ruta_excel = os.path.join(directorio_excel, archivo_excel)

    try:
        df_excel = pd.read_excel(ruta_excel, sheet_name=None)
    except Exception as e:
        print(f"Error al procesar {archivo_excel}: {e}")
        continue

    # Iterar sobre cada hoja del archivo Excel
    for hoja, datos in df_excel.items():
        print("         Procesando hoja ", hoja)
        # Reemplazar ',' y ';' por un número (por ejemplo, 0)
        datos = datos.replace({',': 0, ';': 0})

        # Crear la ruta para guardar el archivo CSV
        nombre_csv = f"{archivo_excel}_{hoja}.csv"
        ruta_csv = os.path.join(directorio_csv, nombre_csv)

        # Guardar los datos en un archivo CSV
        datos.to_csv(ruta_csv, index=False)

print("Proceso completado. Archivos CSV guardados en:", directorio_csv)
