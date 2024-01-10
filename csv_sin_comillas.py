import os
import csv

def procesar_archivo(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'r') as entrada, open(archivo_salida, 'w', newline='') as salida:
        lector_csv = csv.reader(entrada)
        escritor_csv = csv.writer(salida)

        for fila in lector_csv:
            nueva_fila = [campo.replace('"', '').replace(',', '') for campo in fila]
            escritor_csv.writerow(nueva_fila)

if __name__ == "__main__":
    directorio_entrada = "./csv_output"
    directorio_salida = "./csv_output_sin_comillas_comas"

    if not os.path.exists(directorio_salida):
        os.makedirs(directorio_salida)

    archivos_csv = [archivo for archivo in os.listdir(directorio_entrada) if archivo.endswith('.csv')]

    for archivo_csv in archivos_csv:
        ruta_entrada = os.path.join(directorio_entrada, archivo_csv)
        ruta_salida = os.path.join(directorio_salida, archivo_csv)

        procesar_archivo(ruta_entrada, ruta_salida)

    print("Proceso completado.")
