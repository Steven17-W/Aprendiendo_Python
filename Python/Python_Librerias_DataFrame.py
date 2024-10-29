# ------------- DATAFRAME -------------------

#Los modulos o librerias son funciones que an escrito otras personas o compañias, que se pueden usar libremente, incluso yo puedo crear un modulo y compartirlo

#El primer modulo que vamos a importar es OS, que me permite navegar como si estuviese en una consola de comandos

import os

#Para ver donde estoy dentro de la carpeta
"""os.getcwd()"""

#Para ver que hay en el contenido o en mis carpetas utilizo:
"""os.listdir()"""

#Para crear una nueva carpeta uso el metodo siguiente:
"""os.makedirs("Carpeta Mia")"""

#Para poder usar dataframe vamos a activar 2 
#bibliotecas una de ellas es nompy y la otra es pandas, 
# las dos se complementan, y haces cosas diferentes, 
# para crear dataframe existen varias formas.
#Opcion1

import pandas as pd #importo pandas y le pongo sobrenombre pd
import numpy as np #importo numpy y le pongo sobrenombre np

#La primera [forma de crear un dataframe es usando el metodo arrays, y luego guardar]
"""dataframe_1= np.array([[2,4],[6,8],[10,12],[14,16]])"""

dataframe_1= np.array([[3,6,9],[12,15,18],[21,24,27],[30,0,0]])
""""print(dataframe_1)"""

#Para crear el dataframe del arreglo anterior debemos usar pandas 
pd.DataFrame(dataframe_1)

"""print(dataframe_1)"""

#Ahora vamos a cambiarle el nombre a las columnas 
df1=pd.DataFrame(dataframe_1,index=['fila1','fila2','fila3','fila4'],columns=['columna1','columna2','columna3'])
"""print(df1)"""

#---------------------------------- OPCION 2 ----------------------------------------------------

#Ahora creamos un dataframe usando listas

dataframe_2=[[2,4],[6,8],[10,12]]

df2=pd.DataFrame(dataframe_2, index=["Fila1","Fila2","Fila3"],
                 columns=["Columna1","Columna2"])

#Dataframe datos de personas

dataframe_datos=[["Nombre","apellido","edad"],
                 ["Leidy","Peralta","40"],
                 ["Natalia","Garcia","23"],
                 ["Nicol","Garzon","21"],
                 ["Camila","Hernandez","16"]]


#Para el 3er metodo uso los diccionarios de la siguiente manera
#Primero creo 2 listas, listas van hacer columnas del dataframe

"""Ciudades_Colombia=["Bogotá","Medellin","Cali","Barranquilla"]
Ciudades_info=[11000000, 2500000, 2200000, 1300000]

#Ahora creamos los diccionarios con las listas

Ciudades={'ciudades':Ciudades_Colombia, 'Poblacion':Ciudades_info}

#Le paso el metodo pandas
df3=pd.DataFrame(Ciudades)

print(df3)"""


#4 paises con su poblacion y su espectativa de vida . 3 columnas

Paises=["Canada","EEUU","Mexico","España"]
Poblacion=[38000000, 33500000, 12900000, 4700000]
Vida=[82, 78, 75, 83]

#Ahora creamos los diccionarios con las listas

tb={'Paises':Paises, 'Poblacion':Poblacion, 'Vida':Vida}

#Le paso el metodo pandas
df4=pd.DataFrame(tb)

"""print(df4)"""

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Esta es la manera como se suben dataframes constantemente, por que nos permite realizar trabajos mas robustos con poco codigo

estudiantes=pd.read_csv('StudentsPerformance (1).csv')

"""print(estudiantes)"""

#Mostrar las 5 primeras columnas
estudiantes.head()

#mostrar las ultimas filas
estudiantes.tail

#Mostrar filas que yo quiera
estudiantes.head(10)

#Mostrar tamaño del dataframe puedo utilizar el atributo shape
estudiantes.shape

#Puedo mostrar cuantas filas quiera desde el principio uso head
estudiantes.head(60)

#------------------------- metodos de pandas -------------------------------

#Para ver el tamaño y el salto de los datos puedo utilizar el metodo index
estudiantes.index

#para ver las columnas 
estudiantes.columns

#Para ver el tipo de dato de las columnas uso dtype
estudiantes.dtypes

#Para obtener la informacion de todo el dataframe usamos el metodo info
"""print(estudiantes.info())"""


#Las medidas de tendencia central de todo el dataframe
"""print(estudiantes.describe())"""

#-------------------------------- FUNCIONES DE PANDAS ------------------------------------------

len(estudiantes)

max(estudiantes)

max(estudiantes.index)

type(estudiantes)

#redondear valores numericos
round(estudiantes)

#Para mostrar solo una columna 
#estudiantes["gender"]

"""print(estudiantes["math score"])"""

#La otra manera de mostrar una columna es esando el nombre directamente como metodo
estudiantes.gender

#Para Conectar carpetas de google drive 
# from google.colap import drive
#drive.mont("Ruta de archivo")

#Para saber que tipo de dato es ese dataframe uso TYPE

type(estudiantes[['math score','reading score']])

#Para mostrar mas de dos columnas puedo usar el mismo metodo

#print(estudiantes["math score","reading score","lunch"])

#Para crear columnas existen 2 formas, pero el metodo que mas se usa es como si estuvise llamando una columna, vamos a crear una columna que nos muestre la nota de quimica

#estudiantes('Score Chemistry')=70

#print(estudiantes)

#tambien puedo crear valores aleatorios con un arreglo de numpy y luego usarloç

#print(np.arange(0,1000))

nota_quimica=np.arange(0,1000)

estudiantes['score chemistry']=nota_quimica



#Arreglos aleatorios
aleatorio=np.random.randint(1, 100, size=1000)

estudiantes["score chemistry"]=aleatorio

#Alearorios pero con decimales 

print(np.random.uniform(1,100,size=1000))

#Afregemos Incorrecta
estudiantes["Incorrecta"]=0

#para elminimar columna
estudiantes=estudiantes.drop(columns=["Incorrecta"])

print(estudiantes)









