import random as random

def generar_datos():
    datos = []
    for i in range(5000):
        dato={}
        id=random.randint(1,10000)
        referencia=random.choice(["ACH-01","ACH-22","ACH-43"])
        marca=random.choice(["Sony","Rico","Kalley"])
        capacidad=random.randint(100,2000)
        ciudad=random.choice(["Medellín","La Guajira","Santa Fé","Gold Cost","Melbourne"])
        responsable=random.choice(["Santiago Norrea","Alex Cremento","Alan Brito Delgado","Cindy Nero","Jhon Doe"])

        dato=[id,referencia,marca,capacidad,ciudad,responsable]
        datos.append(dato)
    return datos
print(generar_datos())
    