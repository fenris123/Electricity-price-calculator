# -*- coding: utf-8 -*-
"""
Created on Thu May  8 12:57:10 2025

@author: fenris123
"""


#### RECUERDA:  PARA EJECUTAR
###  catalogo = catalogo_esios (), con el termino que se quiera buscar entre comillas, o en blanco para todos.


import requests
import pandas as pd
import os
from dotenv import load_dotenv
import re


#PASO 1   Definimos la funcion, ponemos el token, los headers etc, y acemos la peticion de datos.


def catalogo_esios(indicador_buscado = ""):

    

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
     
    
# PASO 3  filtramos por el termino de busqueda


    for i in range(len(df_indicadores)):
        if indicador_buscado.lower() in df_indicadores['name'].iloc[i].lower():
            print(f"{df_indicadores.loc[i,'id']} -> {df_indicadores.loc[i,'name']}")
       
 
    return (df_indicadores)



