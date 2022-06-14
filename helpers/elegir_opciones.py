import os
from random import choices,shuffle
import csv
from helpers.apertura_de_archivos import ruta_csv

def opciones_random(nombre:str,cant_caracteristicas:int):
    """
     funcion opciones_random
    
    Def:
        Esta funcion retorna las 5 opciones a escribir en la tarjeta, entre las que esta la correcta
        y sus características

    Args:
        nombre(str): nombre del csv del cual se leen las opciones
        cant_caracteristicas(int): cantidad de características de la opción correcta a mostrar
    Ret:
        retorna una lista de las opciones elegidas de manera aleatoria, la opción correcta
        y la lista de sus características
    """
    
    ruta_csv_actual = os.path.join(ruta_csv,'data_set_'+nombre.lower()+'.csv')
    try:
        with open(ruta_csv_actual,'r',encoding='UTF-8') as archivo:
            reader = csv.reader(archivo,delimiter =',')
            next(reader)
            data = list(map(lambda x: x,reader))
        

       
        opciones = choices(data, k=5)
        incorrectas = opciones[1:5]
        correcta = opciones[0]
        caracteristicas = correcta[0:cant_caracteristicas]
        nombre_correcta = correcta[5]
        nombre_incorrectas = list(map(lambda x: x[5],incorrectas))
        
        shuffle(opciones)

        return caracteristicas,nombre_correcta,nombre_incorrectas
    
    except FileNotFoundError:
        return False
