
#Cambiar el tipo de dato de una columna
import pandas as pd

df = pd.read_csv("archivos_problemas_resueltos/datos.csv")

#convertir a string los datos de una columna
df['edad'] = df['edad'].astype(str)
#mostar el tipo de dato del primer elemento de la columna edad
#print(type(df['edad'][0]))

#Reemplazando los dato "dalto" por "Maestro"
df['apellido'].replace("Romero","maestro",inplace=True)

#eliminando las filas con datos faltantes
df = df.dropna()

#eliminando las filas repetidas
df = df.drop_duplicates()

#creando un CSV con el dataframe resultante (limpio)
df.to_csv("archivos_problemas_resueltos/datos_limpios.csv")


