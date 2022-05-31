import os
import csv
import PySimpleGUI as sg

def make_columns(nombre_archivo: str) -> list:
    """
    funcion 'make_columns'
    Def:
        Esta función toma el nombre de un archivo pasado por parámetro, y lo procesa para devolver dos columnas
        para ser implementadas en la parte gráfica. En particular es usada para procesar los archivos con Nick
        y Puntaje para mostrarlos en pantalla.

    Args:
        - nombre_archivo (str): Contiene el string del archivo a ser procesado
    """
    ruta=os.path.join(os.getcwd(),'data','csv',nombre_archivo)
    with open(ruta,"r",encoding='utf-8') as archivo:
        data = csv.reader(archivo)
        columna_nombres = []
        columna_puntajes = []
        for linea in data:
            columna_nombres.append([sg.Text(linea[0], font=("Arial", 10))])
            columna_puntajes.append([sg.Text(linea[1], font=("Arial", 10))])
    return columna_nombres, columna_puntajes