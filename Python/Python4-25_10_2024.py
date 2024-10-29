#importando pandas y numpy

import pandas as pd
import numpy as np

#Utilizando archivo se estudiantes
df_estudiantes=pd.read_csv('StudentsPerformance (1).csv')

#Operaciones en columnas 
#Elegir columna que quiero operar, ojala una columna numerica
'''print (df_estudiantes['reading score'])'''

#Como sumar datos de una columna
df_estudiantes['reading score'].sum()

#Como contar datos de una columna
df_estudiantes['reading score'].count()

#Para calcular el promedio usamos el metodo mean
df_estudiantes['reading score'].mean()

#Para calcular la desviacion estandar de una columna uso el metodo std
df_estudiantes['reading score'].std()

#Para ver los valores maximos de una columna uso el metodo max
df_estudiantes['reading score'].max()

#Para ver los valores minimos de una columna uso el metodo min
df_estudiantes['reading score'].min()

#Para ver la medida de tendencia central de una columna uso el metodo describeç
df_estudiantes['reading score'].describe()

## ------------------ OPERACIONES ENTRE FILAS --------------------------------

'''#Suma
df_estudiantes['math score']+df_estudiantes['writing score']+df_estudiantes['reading score']

#Asi guardo una nueva columna calculada
df_estudiantes['TOTAL']=df_estudiantes['math score']+df_estudiantes['writing score']+df_estudiantes['reading score']
"""print(df_estudiantes)"""

#Promedio de notas 
(df_estudiantes['TOTAL'])/3

#Promedio de notas 
df_estudiantes['PROMEDIO']=(df_estudiantes['TOTAL'])/3

#Asi formateo los numeros para que tengan solo 2 decimales
df_estudiantes.round(2)

#Ahora vamos a contrar elementos por valor
len(df_estudiantes['gender'])

#Para contar cada uno uso el metodo Values.counts
df_estudiantes['gender'].value_counts()

#Para contar la raza y frupos etnicos 
df_estudiantes['race/ethnicity'].value_counts()

#Numero de participacion por cada elemento
df_estudiantes['race/ethnicity'].value_counts(normalize=True)*100'''

#---------------------------------------------------------------------------------------------------

#Agrupar por parental level of education
df_estudiantes['parental level of education'].value_counts()

#Tambien puedo calcular el porcentaje de participación por item
df_estudiantes['parental level of education'].value_counts(normalize=True)*100

#Calcular el numero de participacion por genero
df_estudiantes['gender'].value_counts(normalize=True)*100

#Que psasa si lo uso en una columna numerica
df_estudiantes['math score'].value_counts()

#Ordenar de mayor a menor, con Sort
df_estudiantes.sort_values('math score')
#Asignandolo
df_estudiantes=df_estudiantes.sort_values('math score')

#Descargando archivo - con orden
df_estudiantes.to_csv('df_estudiantes.csv',index = False)

#Ahora vamos a organizar de forma decendente
'''print(df_estudiantes.sort_values('math score', ascending=False))'''

#Tambien podemos ordenar los dataframe, no solo por una columna si no por dos, 
#hay que tener en cuenta que organizara por el primer dato y el segundo sera dependiente
df_estudiantes.sort_values(['reading score','writing score'], ascending=False)

Organizado_Lectura = df_estudiantes.sort_values(['reading score','writing score'], ascending=False)

Organizado_Lectura.to_csv('Organizado_Lectura.csv',index = False)

# De esta manera puedo guardar los datos, y sobre escribir
df_estudiantes.sort_values(['reading score','writing score'], ascending=False,
                           inplace=True)

print(df_estudiantes)


