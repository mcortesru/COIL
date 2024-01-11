import os
import csv

def procesar_archivo(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'r') as entrada, open(archivo_salida, 'w', newline='') as salida:
        lector_csv = csv.reader(entrada)
        escritor_csv = csv.writer(salida)

        for fila in lector_csv:
            # Eliminar comillas y comas de cada campo
            nueva_fila = [campo.replace('"', '').replace(',', '') for campo in fila]
            escritor_csv.writerow(nueva_fila)

if __name__ == "__main__":
    directorio_entrada = "./csvFromExcel"
    directorio_salida = "./csvLimpios"

    # Verificar y crear el directorio de salida si no existe
    if not os.path.exists(directorio_salida):
        os.makedirs(directorio_salida)

    # Verificar si el directorio de entrada existe
    if not os.path.exists(directorio_entrada):
        print("El directorio de entrada no existe. Ejecute primero 'excel_to_csv.py'.")
    else:
        # Procesar archivos si el directorio de entrada existe
        archivos_csv = [archivo for archivo in os.listdir(directorio_entrada) if archivo.endswith('.csv')]

        for archivo_csv in archivos_csv:
            ruta_entrada = os.path.join(directorio_entrada, archivo_csv)
            ruta_salida = os.path.join(directorio_salida, archivo_csv)

            procesar_archivo(ruta_entrada, ruta_salida)

        print("Proceso completado.")
