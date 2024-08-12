#abriendo el archivo con with open
with open("archivos/texto_de_cristian.txt", encoding = "UTF-8") as archivo:
    #leemos el archivo
    contenido = archivo.read()
    
    #mostramos el archivo
    print(contenido)
    
#no es necesario cerralo cunado usamos with open
    
