import os
from random import choices,shuffle
import csv

def opciones_random(nombre:str,correcta:str):
    """
     funcion opciones_random
    
    Def:
        Esta funcion crea una ventana con los atributos pasados y crea un loop que permite la interacción con la misma

    Args:
        nombre(str): nombre del csv del cual se leen las opciones
        correcta(str): es la opcion correcta de entre todas las otras opciones a retornar
    Ret:
        retorna una lista de las opciones elegidas de manera aleatoria, mas la opcion correcta
    """
    
    archivo=os.path.join(os.getcwd(),'data','csv',nombre)
    try:
        data = open(archivo,'r',encoding='UTF-8')
    except FileNotFoundError:
        exit(1)
    else:
        reader = csv.reader(data,delimiter =',')
        next(reader)
        opciones = list(map(lambda x: x[5],reader))
        data.close()

        opciones.remove(correcta)
        opciones = choices(opciones,weights=None, cum_weights=None, k=4)
        opciones.append(correcta)
        shuffle(opciones)

        return opciones