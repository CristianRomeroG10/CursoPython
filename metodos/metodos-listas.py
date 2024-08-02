
lista = list(["hola","cristian",34])

#devuelve la cantidad de elementos de la lista
resultado = len(lista)

#agregando un elemento a la lista
lista.append("JAJAJAJA")

#agregando un elemento a la lista con un indice especifico
lista.insert(2, True)

#agregando varios elementos a la lista
lista.extend([False, 2030])

#Eliminando un elemento de la lista (por su indice) poniendo de indice -1 nos elimina el ultimo,
# con -2 el penultimo y asi sucesivamente
lista.pop(-1)

#Removiendo un elemento por su valor
lista.remove("JAJAJAJA")

#eliminando todos los elementos de la lista
#lista.clear()

#ordenando la lista de forma ascendente, (si usamos el parametro reverse = true o rodena en reversa)
#lista.sort()

#invirtiendo los elementos de una lista 
lista.reverse()

print(lista)
