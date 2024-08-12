with open("archivos/texto_de_cristian.txt","w",encoding = "UTF-8") as archivo:
    #sobreescribiendo el archivo
    #archivo.write("JAJAJAJA te la recontra teclee")
    
    #agregando 2 lineas con writeline()
    archivo.writelines(["- Hola como andas?\n","- misericordia\n"])
    #agregando otras 2 lineas
    archivo.writelines(["- no se porque dijiste eso\n","- yo tampoco"])
    
    
    