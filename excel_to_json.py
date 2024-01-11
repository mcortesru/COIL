import pandas as pd
import sys
import os  # Importa el módulo os

# Lee el archivo Excel
excel_file_path = sys.argv[1]
excel_file = pd.ExcelFile(excel_file_path)

# Obtén los nombres de las hojas
sheet_names = excel_file.sheet_names

# Ruta del directorio para guardar los archivos JSON
jsons_dir = './jsonsFromExcel'

# Verifica si el directorio existe, si no, créalo
if not os.path.exists(jsons_dir):
    os.makedirs(jsons_dir)

# Itera sobre las hojas
for sheet_name in sheet_names:
    # Lee la hoja
    df = excel_file.parse(sheet_name)

    # Convierte el DataFrame a formato JSON
    json_data = df.to_json(orient='records')

    # Calcula el número de archivos necesarios
    num_files = len(df) // 250000 + (len(df) % 250000 != 0)

    # Itera sobre los archivos
    for i in range(num_files):
        # Modifica la ruta para guardar en jsons_dir
        json_file_path = os.path.join(jsons_dir, f'{excel_file_path.split("/")[-1]}_{sheet_name}_{i}.json')
        with open(json_file_path, 'w') as json_file:
            json_file.write(df.iloc[i*250000:(i+1)*250000].to_json(orient='records'))