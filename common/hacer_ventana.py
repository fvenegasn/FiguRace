from typing import Any
import PySimpleGUI as sg

def default_update(*args):
    pass

def crear_ventana(name:str,layout:list,acciones:Any,evaluate_extra=default_update,update_windows=default_update,*args,**kwargs):
    """
    funcion crear_ventana
    
    Def:
        Esta funcion crea una ventana con los atributos pasados y crea un loop que permite la interacción con la misma

    Args:
        name(str): nombre de la ventana a crear
        layout(list): contenido de la ventana a crear
        acciones(funcion): funcion que contiene la logistica de la ventana a crear
    """
    tiempo = 900 if name == "Pantalla de Juego"  else None

    window = sg.Window(name,layout,finalize=True)
    loop = True
    while loop:
        event,values = window.read(timeout=tiempo)
        match event:
            case None |sg.WIN_CLOSED:
                break
        window.Hide()
        loop = acciones(event,values)
        window.UnHide()
        update_windows(window)
    window.close()   

