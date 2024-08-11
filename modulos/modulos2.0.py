# si el modulo estuviera dentro de una carpeta en la misma ruta se importa asi
#import funciones_buenas.saludar as m_saludar

import sys 
sys.path.append("/Users/cristianguillermoromerogarcia/Desktop/Programacion/Python/CursoPython/funciones_buenas")
import saludar as modulo_saludo
print(modulo_saludo.saludar("Cristian"))