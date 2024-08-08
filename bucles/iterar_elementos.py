
animales = ["gato","perro","loro","cocodrilo"]
numeros = (52,16,14,72)

#Recorriendo la lista animales
for animal in animales:
    print(f"Ahora la variable animasl es igual a: {animal}")

#Recorriendo la lista numeros y muñtiplicando cada valor por 10
for numero in numeros:
    resultado = numero * 10
    print(resultado)
    
#iterando 2 listas del mismo tamaño al mismo tiempo 
for animal,numero in zip(animales,numeros):
    print(f"recorriendo la lista 1: {animal}")
    print(f"reccorinedo la lista 2: {numero}")
    
#iterar en un rando (si se pone solo un numero se itera desde cero hasta el numero)
#for num in range(10,20):
#    print(num)

#forma no optima de recorrer una lista por su indice (no funciona en conjuntos)
for num in range(len(numeros)):
    print(numeros[num])
    
#forma correcta de recorrer una lista por su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"el indice es: {indice} y el valor es: {valor}")
    
#usando el for/else
for numero in numeros:
    print(f"ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print("el bucle termino")
    
#todo lo anteriror funciona exactamente igual con las tuplas y conjuntos