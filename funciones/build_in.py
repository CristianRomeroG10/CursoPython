
numeros = [4,7,1,42,15,30]

#encontranso el numero mayor en una lista
numero_mas_alto = max(numeros)
print(numero_mas_alto)

#encontranso el numero menor en una lista
numero_mas_bajo = min(numeros)
print(numero_mas_bajo)

#redondeando de 6 decimales a 2 numeros
numero = round(12.345678, 2)
print(numero)

#retorna False -> 0, vacio o False, \ True -> distinto a 0. True, cadena
resultado_bool = bool([13,45,"jdkkd"])

print(resultado_bool)

#retorna true si todos los valores son verdaderos
resultado_all = all([231,"true",[44,22]])
print(resultado_all)

#suma todos los valores de un iterable
suma_total = sum(numeros)
print(suma_total)