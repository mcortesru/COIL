import os
import json

def convertir_a_string(objeto_json):
    for clave, valor in objeto_json.items():
        if isinstance(valor, (int, float, bool)):
            objeto_json[clave] = str(valor)
        elif isinstance(valor, dict):
            objeto_json[clave] = convertir_a_string(valor)
    return objeto_json

def procesar_archivo(input_path, output_path):
    with open(input_path, "r") as f:
        datos = json.load(f)

    datos = [convertir_a_string(objeto) for objeto in datos]

    with open(output_path, "w") as f:
        json.dump(datos, f, indent=4)

def main():
    # Directorio de entrada y salida
    input_directory = "./jsonsFromExcel/"
    output_directory = "./jsonsLimpios/"

    # Verifica si el directorio de salida existe, si no, créalo
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Verifica si el directorio de entrada existe
    if not os.path.exists(input_directory):
        print("El directorio de entrada no existe. Ejecute primero 'excel_to_json.py'.")
        return

    # Listar archivos en el directorio de entrada
    archivos_json = [archivo for archivo in os.listdir(input_directory) if archivo.endswith(".json")]

    # Procesar cada archivo
    for archivo in archivos_json:
        input_path = os.path.join(input_directory, archivo)
        output_path = os.path.join(output_directory, archivo)

        procesar_archivo(input_path, output_path)

if __name__ == "__main__":
    main()
