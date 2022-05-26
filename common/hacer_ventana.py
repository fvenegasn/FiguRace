from typing import Any
import PySimpleGUI as sg

def crear_ventana(name:str,layout:list,acciones:Any):
    """
    funcion crear_ventana
    
    Def:
        Esta funcion crea una ventana con los atributos pasados y crea un loop que permite la interacción con la misma

    Args:
        name(str): nombre de la ventana a crear
        layout(list): contenido de la ventana a crear
        acciones(funcion): funcion que contiene la logistica de la ventana a crear
    """
    
    window = sg.Window(name,layout,finalize=True)
    
    loop = True
    while loop:
        event,values = window.read()
        match event:
            case None |sg.WIN_CLOSED:
                break
        window.Hide()
        loop = acciones(event,values)
        window.UnHide()
    window.close()   

