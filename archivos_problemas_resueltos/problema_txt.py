
#2 listas, una con nombres otra con apellidos
nombres = ["Cristian","Gael","Eliot","Lily","Cookies"]
apellidos = ["Romero","Romero","Garcia","Garcia","Romero"]

#Registrar esta información en un txt de forma óptima

with open("archivos_problemas_resueltos/nombres_y_apellidos.txt","w" ) as arch:
    arch.writelines("Los datos son: \n\n")
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n--------------\n")for n,a in zip(nombres,apellidos)]
    
    