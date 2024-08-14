
import re

#detectando un numero CABA y ocultandolo
texto = "Hola Pedro, mi numero es: +52 55 4342-1492 y tambien +52 55 2922-3334 "

pattern = r"\+\d{2}\s\d{2}\s\d{4}-\d{4}"

reemplazo = re.sub(pattern,"numero oculto",texto)

print(reemplazo)