import re

texto = '''Hola maestro. esta es la cadena 1. Como estas mi capitan
Esta es la linea 223598 de texto.
Esta es la linea abababab2 de textoabababab.
Y esta es la final (linea 3) definitiva mi capitan
'''

#Haciendo una busqueda simple 
resultado = re.search("Hola",texto)
#ejemplos con re.findall
#resultado = re.findall("la",texto)
#resultado = re.findall("Esta",texto,flags=re.IGNORECASE)

#\d -> busca digitos numericos del 0 - 9
#resultado = re.findall(r"\d",texto)

#\D -> busca TODO menos digitos numericos 
#resultado = re.findall(r"\D",texto)

#\w -> busca caracteres alfanumericos [a-z A-Z 0-9 _ ]
#resultado = re.findall(r"\w",texto)

#\W-> busca TODO menos caracteres alfanumericos 
#resultado = re.findall(r"\W",texto)

#\s-> busca espacios en blanco -> espacios, tabs, saltos de linea
#resultado = re.findall(r"\s",texto)

#\S-> busca TODO menos espacios en blanco -> espacios, tabs, saltos de linea
#esultado = re.findall(r"\S",texto)

#. -> busca TODO menos saltos en linea
#resultado = re.findall(r".",texto)

#\n -> busca TODO menos saltos en linea
#resultado = re.findall(r"\n",texto)

#\ -> cancelar caracteres especiales, cancelando la funcion del punto y buscando puntos 
#resultado = re.findall(r"\.",texto)

#armando una cadena que busque un numero, seguido de un punto y un espacio
#resultado = re.findall(r'\d\.\s',texto)

#^ -> busca el comienzo de una linea Buscando Hola al principio de la linea
#resultado = re.findall(r'^Hola',texto)
#flags=re.M activa la multilinea (igual puede ser flags=re.MULTILINE)
#resultado = re.findall(r'^Esta',texto,flags=re.M)

#$ -> busca el comienzo de una linea Buscando Hola al principio de la linea
#resultado = re.findall(r'capitan$',texto,flags=re.M)

#{n} -> busca n cantidad de veces el valor se la izquierda
#resultado = re.findall(r'\d{3}',texto)

#{n,m} -> busca al menos n, como maximo m
#resultado = re.findall(r'\d{2,4}',texto)
#resultado = re.findall(r'ab{2,4}',texto)
#resultado = re.findall(r'(ab){2}',texto)
#resultado = re.findall(r'[ab]{2}',texto)

#{n,m} -> busca al menos n, como maximo m
resultado = re.findall(r'\d{2,4}|Hola',texto)


print(resultado)
