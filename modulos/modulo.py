#importando el modulo y asignandole el nombre ms
import modulo_saludar as ms
#desde este modulo, importamos dos funciones y les cambiamos el nombre
from modulo_saludar import saludar as saludar_normal, saludar_raro as saludar_como_coscu

#aludo = ms.saludar("Gael")
hola_jaz = saludar_normal("Jazmin")
saludo_raro = saludar_como_coscu("Memo")

print(hola_jaz)
print(saludo_raro)

#para ver las propiedades y metodos en el namespace
#print(dir(ms))

#accedemos al nombre de este modulo
#print(__name__)

#accedemps al nombre del modulo llamado
#print(ms.__name__)
