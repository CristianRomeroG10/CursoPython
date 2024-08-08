#creando una función de 3 parametros

def frase(nombre,apellido,adjetivo):
    return f"Hola {nombre} {apellido}, eres muy {adjetivo}"

#pasandole valores a los argumentos
#frase_resultante = frase("Cristian","Romero","inteligente")

#utilizando keyword arguments
frase_resultante = frase(adjetivo = "Capo",nombre = "Cristian",apellido= "Romero")
print(frase_resultante)

#creando la misma función con un parametro opcional y un valor por defecto
def frase_dos(nombre,apellido,adjetivo = "tonto"):
    return f"Hola {nombre} {apellido}, eres muy {adjetivo}"

frase_resultante2 = frase_dos("Cristian","Romero","Bacano") #el valor puede ser cambiado a pesar de ser definido en un principio
print(frase_resultante2)