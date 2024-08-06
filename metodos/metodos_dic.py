
diccionaro = {
    "nombre": "Cristian",
    "Apellido": "dalto",
    "subs": 1000000
}

#devolvemos las claves (tambien nos sirve para iterar)
#nos devuelve un valor dict_items
claves = diccionaro.keys()

#obteniendo un valor con get(), (si no encuentra nada el programa continua)
obtener_subs = diccionaro.get("subs")

#eliminando todo del diccionario
#diccionaro.clear()

#eliminando elementos del diccionario
diccionaro.pop("subs")

#obteniendo un delemento dict_item terable
diccionario_iterable = diccionaro.items()
print(diccionario_iterable)