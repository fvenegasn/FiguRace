import pandas as pd
import PySimpleGUI as sg
import os
from common.paths import ruta_csv

def hacer_tabla(title,nivel:str):
    """
    función 'hacer_tabla'
    Def:
        Esta funcion recibe el titulo y un nivel y genera una tabla con los mejores 20 puntajes de la dificultad recibida

    Args:
        title(str): título que tendrá la tabla
        nivel(str): nivel del cual generar la tabla
    """
    ruta=os.path.join(ruta_csv,'puntajes_'+nivel+'.csv')
    usuarios,puntajes = elegir_mejores(20,ruta)
    datos=[
        [
        sg.Column(([sg.Text(usuario, font=("Arial", 12),background_color='white')]for usuario in usuarios),background_color='white'),
        sg.Column(([sg.Text(puntaje, font=("Arial", 12),background_color='white')]for puntaje in puntajes),background_color='white')
        ]
    ]
    
    layout_tabla = [
        [sg.Column(datos,scrollable=True,vertical_scroll_only=True,element_justification='left',background_color='grey')],
    ]

    tabla=sg.Frame(title=title,layout=layout_tabla,font=('Arial',12),background_color='pink')
    return tabla

def elegir_mejores(cant:int,ruta:str):
    """
    funcion 'elegir_puntajes'
    Def:
        Esta función recibe una cantidad pasada por parámetro, y procesa un archivo csv obteniedo 
        los 'cant' mejores valores en el mismo
        En particular es usada para procesar los archivos con Nick y Puntaje para mostrarlos en pantalla.

    Args:
        - cant(int): es la cantidad de valores a tomar
        - ruta(str): Contiene la ruta del archivo a ser procesado

    Retorna dos lista, una con los valores y otra con los nick
    """
    df=pd.read_csv(ruta)
    df=df.sort_values(by='Puntaje',ascending=False).head(cant)

    return list(df['Nick']),list(df['Puntaje'])

