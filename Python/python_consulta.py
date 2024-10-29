import pandas as pd #importo pandas y le pongo sobrenombre pd
import numpy as np #importo numpy y le pongo sobrenombre np


Canciones=pd.read_csv('classic_rock_playlist.csv')
"""print(Canciones)"""

#Mostrar las 5 primeras columnas
"""print(Canciones.head())"""

#mostrar las ultimas filas
Canciones.tail

#Mostrar filas que yo quiera
Canciones.head(10)

#Mostrar tamaño del dataframe puedo utilizar el atributo shape
Canciones.shape

#Puedo mostrar cuantas filas quiera desde el principio uso head
Canciones.head(60)

#Para ver el tamaño y el salto de los datos puedo utilizar el metodo index
Canciones.index

#para ver las columnas 
Canciones.columns

#Para ver el tipo de dato de las columnas uso dtype
Canciones.dtypes

#Para obtener la informacion de todo el dataframe usamos el metodo info
print(Canciones.info())


#Las medidas de tendencia central de todo el dataframe
print(Canciones.describe())





