# -*- coding: utf-8 -*-
"""
Created on Thu May  8 12:57:10 2025

@author: fenris123
"""

import requests
import pandas as pd
import os
from dotenv import load_dotenv
import re


#PASO 1   Definimos la funcion, ponemos el token, los headers etc, y acemos la peticion de datos.


def catalogo_esios():

  

    load_dotenv(r'C:\espaciopython\enviroments\tokens.env')  #EN ESTE ARCHIVO DEBEN ESTAR LOS DATOS DE CONEXION
    Token_esios = os.getenv("TOKEN_ESIOS")

    
    headers = {'Accept':'application/json; application/vnd.esios-api-v2+json',
           'Content-Type':'application/json',
           'Host':'api.esios.ree.es',
           'x-api-key': Token_esios,
     
           }
    
    end_point = 'https://api.esios.ree.es/indicators'
    response = requests.get(end_point, headers=headers).json() 
  
# PASO 2 creamos un dataframe  del contenido de response['indicators'] Y LO LIMPIAMOS DE RESTOS DE HTML EN LA DESCRIPCION

    
    df_indicadores = (pd.json_normalize(data=response['indicators'], errors='ignore'))  # similar a pd.Dataframe pero mejor
    
        
    df_indicadores["description"] = df_indicadores["description"].apply(
    lambda x: re.sub(r"<.*?>", "", x) if isinstance(x, str) else x
)
           
    return (df_indicadores)


##  CONTINUAR POR AQUI:  METER ESTO DE ALGUNA FORMA EN LA FUNCION.
##  AHORA MISMO HABRIA QUE EJCUTARLO INDEPENDIENTEMENTE

#    catalogo = catalogo_esios

#    for i in range(len(catalogo)):
#       if catalogo['name'].iloc[i].str.contains('uclear'):
#          print (f"{catalogo.loc[i,'id']} -> {catalogo.loc[i,'name']}")