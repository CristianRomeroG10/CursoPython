
#Le pedimos al usuario que nos pase una frase (o varias)
frase = input("dime una frase y te cho,alculo cuento tardarias si tuvieras que decirla: ")

#creamos una lista con todas las palabras de la frase (se separan cada que haya un espacio en blanco)
palabras_separadas = frase.split(" ")

#Usamos len() para ver la cantidad de elementos que hay en las lista
cantidad_de_palabras = len(palabras_separadas)

#En caso de que tarde mas de un minuto en decirlo, le decimos que pare un poco
if cantidad_de_palabras > 120:
    print("Para flaco tampoco te pedi un testamento")


#Calculamos cuanto tardaria n decir las pabras y se lo decimos
print(f"Dijiste {cantidad_de_palabras} palabras y tardarias {cantidad_de_palabras/2} segundos en decirlo")
print(f"Dalto lo diria en {cantidad_de_palabras/2 * 1.3} segundos ")

