# COIL grupo 5 Análisis de Factibilidad técnica de convertir una base de datos horizontal a vertical
- Mario Cortés Ruiz

## Introducción
El presente informe aborda el proyecto de análisis de factibilidad técnica para la conversión de una base de datos horizontal a vertical.

La elección de SQL Server (como base de datos horizontal) y Azure Cosmos DB (como base de datos vertical) se fundamenta en la posibilidad de realizar una comparación directa entre dos entornos gestionados por Microsoft.

Para simular el contexto, creamos unos ficheros .xlsx donder generamos datos aleaotrios con los que trabajar

Pero poder insertar los datos a SQL Server, fue necesario tener los datos en formato .csv, y para poder incluirlos en Azure Cosmos DB, fue necesario tener los datos en formato .json.

Así que, una vez que contábamos con los .xlsx, fue necesario desarrollar una serie de scripts en python para limpiar los datos y obtenerlos en el formato deseado

## Orden de ejecución
## 1
`excel_to_json.py`
> ES NECESARIO INDICARLE EL FICHERO QUE SE DESEA PROCESAR

Este fichero guarda los .json a partir del .xlsx en `./jsonsFromExcel`
Además, estos ficheros .json contienen como máximo 250.000 objetos (porque es el límite de Cosmos DB)

## 2
`limpiar_jsons.py`
Este fichero limpia valores enteros, booleanos... De forma que son aptos para Cosmos DB.
Los ficheros limpios se guardan en `./jsonsLimpios`

## 3
`excel_to_csv.py`
Este fichero guarda los .json a partir de los .xlsx en `./csvFromExcel`

## 4
`limpiar_csv.py`
Este fichero elimina comillas y comas de cada campo, de forma que tienen un formato válido.
Los ficheros limpios se guardan en `./csvLimpios`
