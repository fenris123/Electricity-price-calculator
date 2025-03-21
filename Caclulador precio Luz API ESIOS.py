# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 11:38:06 2025

@author: fenris123
"""



import os
import requests
import json
from dotenv import load_dotenv




load_dotenv('C:\espaciopython\enviroments\tokens.env')  #EN ESTE ARCHIVO DEBEN ESTAR LOS DATOS DE CONEXION

# Obtener el token desde el archivo .env
Token_esios = os.getenv("TOKEN_ESIOS")

# Headers para la autenticación
headers = {
    'Host': 'api.esios.ree.es',
    'x-api-key': Token_esios
}

# URL base y endpoint
URL_BASE = 'https://api.esios.ree.es/'
ENDPOINT = 'indicators/'

# ID del indicador
INDICATOR = '600'
url = URL_BASE + ENDPOINT + INDICATOR

start_date = input("Introduzca la fecha de inicio (YYYY-MM-DD): ")
end_date = input("Introduzca la fecha de final (YYYY-MM-DD): ")

params = {
    'start_date': f'{start_date}T00',
    'end_date': f'{end_date}T23'
}


# Realizar la solicitud GET
res = requests.get(url, headers=headers, params=params)

# Procesar la respuesta en formato JSON
data = res.json()

# Filtrar los datos para obtener solo los registros de "España" (geo_id = 3)
filtered_data = [record for record in data.get('indicator', {}).get('values', []) if record.get('geo_id') == 3]

# Guardar los datos filtrados en un archivo .json
with open('filtered_data.json', 'w') as f:
    json.dump(filtered_data, f, indent=4)

print("Datos filtrados por España y guardados en filtered_data.json")


