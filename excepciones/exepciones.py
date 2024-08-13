#Creando la funcion que suma numeros
def sumar_dos():
    #iniciando un bucle
    while True:
        a = input("Numero 1: ")
        b = input("Numero 2: ")
        #intentando convertirlos a entero y sumarlos
        try:
            resultado = int(a) + int(b)
        #si lanzo una excepción, pedirle que reingrese los datos
        except ValueError as e:
            print("Te pedi un numero salame, no te hagas el gracioso") 
            print(f"ERROR: {e}")
        #si todo salio bien terminamos el bucle
        else: 
            break
        #esto se ejecuta siempre
        finally:
            print("Manejo de excepcion finalizado")     
        
    #retornamos el resultado
    return resultado

#imprimimos el resultado
print(sumar_dos())