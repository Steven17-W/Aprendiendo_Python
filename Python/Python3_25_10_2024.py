#importando pandas y numpy

import pandas as pd
import numpy as np

#Utilizando archivo se estudiantes
df_estudiantes=pd.read_csv('StudentsPerformance (1).csv')

"""print(df_estudiantes)"""

#Sigamos con la creacion de columnas usando el metodo assing o el metodo insert
#Si quiero agregar varias columnas uso assing y tambien si quiero sobreescribir una columna

#Creando notas de fisica y filosofia aleatorio y guardamos en variable
filosofia_score=np.random.randint(1, 100, size=1000)
fisica_score=np.random.randint(1, 100, size=1000)

#Ahora le ponemos un indice a cada fila para saber sonde va en el dataframe
filosofia_nota=pd.Series(filosofia_score, index=np.arange(0,1000))
fisica_nota=pd.Series(fisica_score, index=np.arange(0,1000))

#Ahora lo que voy hacer es poner las nuevas columnas a mi dataframe, usando assing
"""print (df_estudiantes.assign(filosofia_score=filosofia_nota, fisica_score=fisica_nota))"""

df_estudiantes=df_estudiantes.assign(filosofia_score=filosofia_nota, fisica_score=fisica_nota)


#Ahora vamos a utilisar el metodo insert, que es diferente ya que me permite especificar donde voy a insertar esa columna
#Al usar el metodo insert, tengo que tener cuidado por que no me devuelve copias si no el cambio queda realizado

df_estudiantes.insert(1,'ED_SCORE', fisica_nota)
print(df_estudiantes)

