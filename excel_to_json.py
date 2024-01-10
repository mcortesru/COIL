import pandas as pd
import sys

# Lee el archivo Excel
excel_file_path = sys.argv[1]
excel_file = pd.ExcelFile(excel_file_path)

# Obtén los nombres de las hojas
sheet_names = excel_file.sheet_names

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
        # Crea un nuevo fichero JSON con el path del archivo de entrada, el nombre de la hoja y el número de archivo
        with open(f'{excel_file_path.split("/")[-1]}_{sheet_name}_{i}.json', 'w') as json_file:
            json_file.write(df.iloc[i*250000:(i+1)*250000].to_json(orient='records'))