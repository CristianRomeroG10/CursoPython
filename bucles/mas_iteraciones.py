#creando las listas
frutas = ["banana","manzana","ciruela","durazno","pera","naranja","granada"]
cadena = "hola cristian"
numeros = [2,5,8,10]
#evitando que se coma una manzana con la sentencia continue
for fruta in frutas:
    if fruta == "durazno":
        continue
    print(f"Me voy a comer una {fruta}")
    
print("------------------------")
for fruta in frutas:
    print(f"Me voy a comer una {fruta}")
    if fruta == "pera":
        break
else:
    print("terminado")
    
print("------------------------")

#recorrer cadena de texto
for letra in cadena:
    print(letra)
    
#for en una sola linea de codigo 
numeros_duplicados = [x*2 for x in numeros] #(duplicamos los numeros)
print(numeros_duplicados)


