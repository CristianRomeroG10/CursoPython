
#creando un conjunto con set()
conjunto = set(["Dato 1",])

#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato 1","dato 2"])
conjunto2 = {conjunto1, "dato 3"}
#print(conjunto2)

#Teoria de conjuntos 
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

#Verificando si es un subconjunto
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1

#Verificando si es un superconjunto
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto1 > conjunto2

#verificar si hay algun numeró en comun (si hay por lo menos un numero igual mandara false)
resultado = conjunto2.isdisjoint(conjunto1)

print(resultado)

