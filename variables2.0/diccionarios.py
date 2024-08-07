
#creando diccionarios con dict()
diccionario = dict(nombre="Cristian",apellidos="Romero")


#las listas no pueden ser claves, solo las tuplas y utilizamos frozenset para meter conjuntos
diccionario = {("dalto","rancio"): "jsjsjs"}
diccionario = {frozenset(["Cristian","Rancio"]): "jajaja"}
#diccionario = {["Gael","Rancio"]: "jejeje"} esto no se puede proque la lista es mutable
#diccionario = {{"Gael","Rancio"}: "jejeje"} tampoco se puesde porque no es hashable por eso usamos el frozen set

#creando diccionario con fromkeys()
#recordando que los diccionarios son iterables si nosotros lo dejamos como esta a continuación nos imprime lo siguiente
diccionario = dict.fromkeys("nombre","apellido")
#resultado en consola: {'n': 'apellido', 'o': 'apellido', 'm': 'apellido', 'b': 'apellido', 'r': 'apellido', 'e': 'apellido'}
#Para evitar eso se pone como una lista
diccionario = dict.fromkeys(["nombre","apellido","suscriptores"])

#creando diccionario con fromkeys() valor por defecto: none
diccionario = dict.fromkeys(["nombre","apellido"])

#creando diccionario con fromkeys() cambiando el valor por defecto a "no se"
diccionario = dict.fromkeys(["nombre","apellido"], "No se")

print(diccionario)
