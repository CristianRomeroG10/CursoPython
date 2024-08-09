#falto el profe y los pibes van a armar la clase

#pedir el nombre y la edad de los compañeros que vinieron hoy a clase

#funcion para obtener al asisitente y al profesor segun la edad
def obtener_compañeros(cantidad_de_compañeros):
    
    #creando lista con os compañeros
    compañeros = []
    
    #ejecutando un for parapedir información de cada compañero
    for i in range(cantidad_de_compañeros):
        nombre = input("ingrese le nombre del compañero: ")
        edad = int(input("ingrese la edad del compañero: oliver"))
        compañero = (nombre,edad)
        
        #agregando la información a las lista
        compañeros.append(compañero)
        
    #ordenandolos de menor a mayor segun su edad
    compañeros.sort(key= lambda x:x[1])
    
    #compañeros[x] devielve una tupl con (nombre,edad) y despues accedemos al nombre
    #para definir asistente y profesor
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    
    #retornamos una tupla
    return asistente,profesor

#desempaquetamos lo que nos retorna la función
asistente,profesor = obtener_compañeros(5)

#mostrando el resultado
print(f"El profesor es_ {profesor} y su asistente es {asistente}")


