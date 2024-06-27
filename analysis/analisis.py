from generators.generadorConsumo import generar_datos

import pandas as pd

def analizar_datos():
    datos=generar_datos()
    tabla=pd.DataFrame(datos,columns=['id','referencia','marca','capacidad','ciudad','responsable'])
    tabla.to_csv("Archivo.csv",index=False)

analizar_datos()

