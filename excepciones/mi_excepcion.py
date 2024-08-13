#Creando mi propia excepción personalizada
class MiException(Exception):
    def __init__(self, err):
        print(f"Impresionante, cometiste el siguiente error: {err}")
        
#Lanzando mi propia excepción        
#raise MiException("JAJAJAJAJA persona poco culta")

#manejandola
try:
    raise MiException("JAJAJAJAJA persona poco culta")
except:
    print("como vas a cometer ese error?")

