import pandas as pd
import PySimpleGUI as sg
import os
from common.paths import ruta_csv

def hacer_tabla(title:str,columna1:list,columna2:list):
    """
    función 'hacer_tabla'
    Def:
        Esta funcion recibe el titulo, y los valores de las dos columnas para tabla 

    Args:
        title(str): título que tendrá la tabla
        columna1(list): nivel del cual generar la tabla
        columna2(list): nivel del cual generar la tabla
    """
    datos=[
        [
        sg.Column(([sg.Text(valor, font=("Arial", 12),background_color='white')]for valor in columna1),background_color='white'),
        sg.Column(([sg.Text(valor, font=("Arial", 12),background_color='white')]for valor in columna2),background_color='white')
        ]
    ]
    
    layout_tabla = [
        [sg.Column(datos,scrollable=True,vertical_scroll_only=True,element_justification='left',background_color='grey',size=(200,200))],
    ]

    tabla=sg.Frame(title=title,layout=layout_tabla,font=('Arial',12),background_color='pink',size=(180,180))
    return tabla

def elegir_mejores(cant:int,data_frame:pd.DataFrame,columna:str):
    """
    funcion 'elegir_mejores'
    Def:
        Esta función recibe una cantidad pasada por parámetro, y procesa un un DataFrame obteniedo 
        los 'cant' mejores valores en el mismo
        En particular es usada para procesar los archivos con Nick y Puntaje para mostrarlos en pantalla.

    Args:
        - cant(int): es la cantidad de valores a tomar
        - data_frame(pd.DataFrame): DataFrame a ser procesado
        - columna(str): Columna por la cual se ordena
    Retorna un DataFrame de maximo 'cant' elemetos ordenados de forma descendente 
    por la columna pasada por parámetro
    """
    df=data_frame.sort_values(by=columna,ascending=False).head(cant)
    return df

def mejores_promedios(nivel:str):
    """
    funcion 'mejores_promedios'
    Def:
        Esta función recibe un nivel por parámetro, y retorna una tabla con, como maximo, los 20 mejores
        puntajes promedios por usuario del nivel.
        Procesa, si existe, un archivo con todos los puntajes de ese nivel, generando un DataFrame con 
        los promedios por usuario.
    Args:
        - nivel(str): Nivel al hacer tabla

    """
    ruta=os.path.join(ruta_csv,'puntajes_'+nivel+'.csv')
    title='Dificultad '+nivel.title()
    if(os.path.exists(ruta)):
        df=pd.read_csv(ruta)
    else:
        return hacer_tabla(title,['No hay puntajes', 'registrados'],[])
    #Creación del dataframe con los promedios
    usuarios=list(df.groupby(['Nick']).size().keys())
    datos=[(usuario,round(df[df['Nick']==usuario]['Puntaje'].mean(),2))for usuario in usuarios]
    promedios=pd.DataFrame(datos,columns=['Nick','Promedio'])

    promedios=elegir_mejores(20,promedios,'Promedio')
    tabla=hacer_tabla(title,promedios['Nick'],promedios['Promedio'])
    return tabla

def mejores_puntajes(nivel:str):
    """
    funcion 'mejores_promedios'
    Def:
        Esta función recibe un nivel por parámetro, y retorna una tabla con, como maximo, los 20 mejores
        puntajes del nivel.
    Args:
        - nivel(str): Nivel al hacer tabla

    """
    ruta=os.path.join(ruta_csv,'puntajes_'+nivel+'.csv')
    title='Dificultad '+nivel.title()
    if(os.path.exists(ruta)):
        df=pd.read_csv(ruta)
    else:
        return hacer_tabla(title,['No hay puntajes', 'registrados'],[])
    puntajes=elegir_mejores(20,df,'Puntaje')
    
    tabla=hacer_tabla(title,puntajes['Nick'],puntajes['Puntaje'])
    return tabla