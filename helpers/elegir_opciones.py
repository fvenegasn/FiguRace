import os
from random import sample
import csv
from common.paths import ruta_csv

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
            columnas=next(reader)
            data = list(map(lambda x: x,reader))
        
        exito = False
        while (not exito):
            opciones = sample(data, k=5)
            nombres_opciones = list(map(lambda x:x[5],opciones))
            nombres_sin_rep = set(nombres_opciones)
            exito = len(nombres_sin_rep) == len(nombres_opciones)
        
        descartadas = opciones[1:5]
        elegida = opciones[0]
        caracteristicas = elegida[0:cant_caracteristicas]
        opcion_correcta = elegida[5]
        opciones_incorrectas = list(map(lambda x: x[5],descartadas))

        return columnas,caracteristicas,opcion_correcta,opciones_incorrectas
        
    except FileNotFoundError:
        return False
