cadena1 = "hola,maquina,hola,soy,cristian"
cadena2 = "Bienvenido Maquinola"


#Convierte a mayusculas
mayusc = cadena1.upper()

#convirte a minusculas
minusc = cadena2.lower()

#Convierte la primer letra en mayuscula
primer_letra_mayusc = cadena1.capitalize()

#Buscamos una cadena en otra cadena, si no hay coincidencias devuelve -1
busqueda_find = cadena1.find("Cristian")

#Buscamos una cadena en otra cadena, si no hay coincidencias lanza una excepción
busqueda_index = cadena1.index("a")

#si es numerico devueve true, si no devuelve false
es_numerico = cadena1.isnumeric()

#si es alfanumerico devuelve true, su no devolve false
es_alfa_numerico = cadena1.isalpha()

#Contamos coincidencias de una cadena dentro de otra cadena, devuelve la cantidad de veces que coincida
contar_coincidencias = cadena1.count("maquina")

#Contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)

#Verificamos si una cadena empieza con otra cadena dada, si es asi devuelve True
empieza_con = cadena2.startswith("B")

#Verificamos si una cadena termina con otra cadena dada, si es asi devuelve True
termina_con = cadena1.endswith("n")

##Remplaza un pedazo de la cadena dada, por otra dada
#si el valor 1 se encuentra en la cadena original, reemplaza el valor 1 de la misma por el valor 2
#si no el valor 1 no se encuentra en la cadena original, nos regresa la cadena original
cadena_nueva = cadena1.replace("stian","na la cochina")

#Seapar cadenas con la cadena que le pasemos
cadena_separada = cadena1.split(",")


print(cadena_separada) 

