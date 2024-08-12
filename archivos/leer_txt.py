#usando open para abrir n archivo con una codificación universal (utf8)
archivo = open("archivos/texto_de_cristian.txt",encoding="UTF-8")

#Leer archivo completo
archivo_leido = archivo.read()

#Leer linea por linea
#lines = archivo_sin_leer.readlines()

#Leer una sola linea, se puede poner el numero de caracteres para leer .readlnine(numero_de_caracteres)
#linea = archivo.readline()

#cerrar el archivo 
archivo.close()

print(archivo_leido)

