
#forma no ptima de sumar valores
#def suma(lista):
 #   numeros_sumados = 0
  #  for numero in lista:
   #     numeros_sumados = numeros_sumados + numero
    #return numeros_sumados
#resultado = suma(5,3,9,10,20,3)

#forma optima de sumar valores
def suma_total(numeros):
    return sum([*numeros]) #se debe crear la lista

resultado2 = suma_total([5,3,9,10,20,3]) #se le debe pasar una lista

print(resultado2)

#lo mismo de afriba pero utilizando el operador * como argumento (*args)
def suma(nombre, *numeros): #siempre debe pasarse como ultimo parametro
    return f"{nombre}, la suma de tus numero es: {sum(numeros)}"
    

resultado = suma("Cristian",5,3,9,10,20,3)
print(resultado)


