print(" ")
print("Importamos los paquetes necesarios")
print(" ")
#!pip install palmerpenguins
import pandas as pd
import numpy as np
from palmerpenguins import load_penguins

penguins = load_penguins() #Cargamos el dataframe que usaremos para los ejercicios

print("--------------------------------------- Ejercicio 1 ---------------------------------------")
print("Vamos a cargar el conjunto de datos. Muestra por pantalla el número de observaciones ")
print("y sus características. Mira el tipo de datos de cada una de sus columnas.")
print(" ")

print(penguins.shape) 
print("Número de observaciones: ", penguins.shape[0],";  Número de caracteristicas: ", penguins.shape[1])
print(" ")
print(penguins.info()) #El comando info() nos ofrece el tipo de datos de cada columna
print(" ")


print("--------------------------------------- Ejercicio 2 ---------------------------------------")
print("Ya sabemos que este conjunto de datos tiene observaciones NA. Vamos") 
print("a eliminarlas y a verificar que efectivamente no queda ninguno:")
print(" ")
print("Vemos que hay un total de 19 NA.")
print(" ")
print(penguins.isna().sum()) #Vemos que hay un total de 19 NA
penguins.dropna(inplace=True)
print(" ")
print("Utilizando el comando dropna(), eliminamos todas las filas que contengan algún NA.")
print(" ")
print(penguins.isna().sum()) #Sumamos todos los NA de cada columna
print(" ")


print("--------------------------------------- Ejercicio 3 ---------------------------------------")
print("¿Cuántos individuos hay de cada sexo? Puedes obtener la longitud media") 
print("del pico según el sexo:")
print(" ")
print("Agrupamos por la columna 'sex' y contamos el numero de individuos que hay.")
print(" ")
count_sex = penguins.groupby('sex')["sex"].count() #Agrupamos por la columna 'sex' y contamos cuantos individuos hay
print(count_sex)
print(" ")

print("Agrupamos por la columna 'sex' y mediante el comando aggregate() hacemos la media del pico.")
bill_bysex=penguins.groupby("sex").aggregate({
    "bill_length_mm":np.mean}) #Agrupamos por la columna 'sex' y con el comando agregate() hacemos la media de la columna 'bill_length_mm'
print(" ")
print(bill_bysex)
print(" ")
print("Otra manera de hacerlo es mediante el comando discribe(), localizando las columnas")
print("que nos interesan que son 'count' y 'mean'.")

#Mediante esta única linea de código, también podemos sacar por pantalla los dos resultados anteriores.
#Como el resultado que sacamos con el método describe() es una tabla multiíndice, primero filtraremos 
#por la columna "bill_length_mm" y dentro de esta columna, volvemos a filtrar por las columnas
#que nos interesa que son "count" y "mean"
bill_cm_bysex = penguins.groupby('sex').describe().loc[:,"bill_length_mm"].loc[:,("count", "mean")]
print(" ")
print(bill_cm_bysex)
print(" ")


print("--------------------------------------- Ejercicio 4 ---------------------------------------")
print("Vamos a añadir una columna, vamos a realizar una estimación (muy grosera) del área del pico")
print("de los pingüinos (bill) tal como si esta fuese un rectángulo. Esta nueva columnas se") 
print("llama bill_area y debe encontrarse en la última posición. Verifica que es correcto.")
print(" ")
print("Creamos la columna 'bill_area' multiplicando 'bill_length_mm' y 'bill_depth_mm'")
print("Para verificar que es la última columna, utilizaremos el comando 'penguins.columns[-1]'")
print(" ")
bill_area = penguins["bill_length_mm"]*penguins["bill_depth_mm"]
penguins["bill_area"]=bill_area
print(penguins.columns[-1])
print(" ")


print("--------------------------------------- Ejercicio 5 ---------------------------------------")
print("Hagamos algo un poco más elaborado, vamos a realizar una agrupación en función del sexo y de la especie")
print("de cada observación. Queremos obtener solamente la información referente al sexo Femenino.")
#

gr_sex_sp = penguins.groupby(["sex","species"]).describe() #Agrupamos por las columnas 'sex' y 'species' 
                                                           #y utilizamos describe() para obtener información
print(" ")
print("Agrupamos por 'sex' y 'species'")
print(" ")
print(gr_sex_sp)
print(" ")
print("Capturamos solo la información relativa al sexo femenino")
print(" ")
print(gr_sex_sp.loc["female", :]) #Filtramos y nos quedamos solo con la información referente al sexo femenino
print(" ")

print("--------------------------------------- Ejercicio 6 ---------------------------------------")
print("Como ya sabemos, la variable peso, se encuentra en gramos, la pasaremos a kg. Para ello crearemos") 
print("una nueva columna llamada body_mass_kg y eliminaremos body_mass_g.") 
print(" ")
print(penguins)
print(" ")
print("Creamos la columna body_mass_kg y eliminamos la columna body_mass_g")

body_mass_kg=penguins["body_mass_g"]/1000 #Creamos la columna 'body_mass_kg'
penguins["body_mass_kg"]=body_mass_kg #Añadimos esta columna al dataframe

penguins.drop(["body_mass_g"], axis=1, inplace=True) #Eliminamos la columna "body_mass_g" utilizando axis=1 
                                                     #para eliminar una columna y no una fila e inplace=True 
                                                     #para que no nos devuelva una copia sino que el cambio 
                                                     #tenga efecto sobre el dataframe.                                                    
print(" ")
print(penguins)

