#Datos, complejos

#Lista
#Crendo una lista (se puede modificar)
lista = ["Lucas dalto", "Soy dalto", True, 1.89]

#Tupla
#Creando una tupla (no se pueden modificar)
tupla = ("Lucas dalto", "Soy dalto", True, 1.89)

#Esto es valido
lista[3] = "maquinola"

#Esto no es valido
#tupla[3] = "Calvario"

#Conjunto (set)
#Creando un conjunto (set) (no se accede a elementos por indice , no almacenan datos duplicados)
conjunto = {"Lucas dalto", "Soy dalto", True, 1.89}

#print(conjunto[3]) -> no puede acceder al elemento

#diccionario (dict)
#Creando un diccionario (dict) (La estructura es key : value y separamos con comas)
diccionario = {
    'nombre': 'Cristian Romero',
    'Canal':'SoyCris',
    'Esta emocionado': True,
    'altura': 1.73,
    'Dato duplicado': "SoyCris"
}

print(diccionario['altura'] + 2)
print(diccionario['nombre'] + " Garcia")
