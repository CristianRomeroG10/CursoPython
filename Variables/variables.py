#definir una variable y asignar un valor a la variable
numero = 10
#sumar lo que esta guardado  + lo que se indique
numero += 5
#restar lo que esta guardado  + lo que se indique
numero -= 5
print(numero)

nombre = "Cristian"

#Concatenar con signo +
bienvenida = "Hola " + nombre + " ¿Cómo estas?"
print(bienvenida)

# concatenar con f String
#Transforma cualquier tipo de dato que tienes asignado en una variable en string
nombre = "Lucas"
bienvenida = f"Hola {nombre} ¿Cómo estas??"
print(bienvenida)

#se utiliza "del" para borrar datos
del nombre

#operadores de pertenencia (in / not in)
print("Lucas" in bienvenida)  #True
print("Lucas" not in bienvenida ) #False

#Definiendo una variable con camelCase
nombreCompletoDeTuTioMater = "Cristian Romero"
#Definiendo un variable con snake_case
nombre_completo_de_tu_tio_master = "Cristian Romero"