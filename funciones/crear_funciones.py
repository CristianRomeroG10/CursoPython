#creando una funcion simple
#def saludar():
    #print("Hola lucas mi maestro, ¿Como andas?")
    
#ejecutando la función simple
#saludar()

#Creando un funcion que tenga parametros
def saludar(nombre,sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = "titan"
    else:
        adjetivo = "amer"
        
    print(f"Hola {nombre}, mi {adjetivo} ¿Cómo estas?")

saludar("Cristian", "homBre")
saludar("Jazmin","mUjer")
saludar("Gael","no-binario")

#crear una funcion que nos retorne multiples valores
def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    #print(f"cadena: {num_entero}") print personal solo para comprender el funionamiento de la logica
    num = int(num_entero[0])
    #print(f"num: {num} ") print personal solo para comprender el funionamiento de la logica
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return (contraseña,num)
    
#desempaquetando la función
password, primer_numero = crear_contraseña_random(859)
 
 #mostrando lo resultados obtenidos y los datos utilizados para obtenerlo 
print(f"Tu contraseña nueva es: {password}")
print(f"El numero Utilizado para crearla fue: {primer_numero}")

