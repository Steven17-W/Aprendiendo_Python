#importando pandas y numpy

import pandas as pd
import numpy as np

# Web Scraping - vamos a hacerlo simple

datos_futbol=pd.read_csv('https://www.football-data.co.uk/mmz4281/2425/E0.csv')

'''print(datos_futbol)'''

#Ahora voy a cambiarle el nombre a las columnas para poder verla de una mejor manera

datos_futbol.rename(columns={'fecha':'Fecha',
                             'HomeTeam':'Local',
                             'AwayTeam':'Visitante',
                             'FTHG':'Goles locales',
                             'FTAG':'Goles Visitante'})

print(datos_futbol)

'''https://www.football-data.co.uk/mmz4281/2425/E0.csv
https://www.football-data.co.uk/mmz4281/2425/E1.csv
https://www.football-data.co.uk/mmz4281/2425/E2.csv
https://www.football-data.co.uk/mmz4281/2425/E3.csv
https://www.football-data.co.uk/mmz4281/2425/EC.csv'''

#la siguiente estructura a que podemos ver en el link
'https://www.football-data.co.uk/mmz4281/'+'2425'+'/'+'E0'+'.csv'

#La raiz siempre es la misma
ruta='https://www.football-data.co.uk/mmz4281/'

#Lista lo que cambia
Campeonatos=['E0','E1','E2','E3','EC']
enlaces=[]

#Para que esto funcione debo recorrer la lista con un loop a esta practica se le conoce como link dinamico, una vez recorra la lista 
#debo remplazar el valor para que el enlace funcione

for campeonato in Campeonatos:
    df_links=pd.read_csv(ruta + '2425' + '/' + campeonato + '.csv')
    enlaces. append(df_links)

#voy a medir la longitud de la lista 

len(enlaces)

print(enlaces[-1])
