from tkinter import CENTER
from typing import Any
import PySimpleGUI as sg

from common.sessions import sessions

def default_update(*args,**kwargs):
    pass

def crear_ventana(name:str,layout:list,acciones:Any,update_windows=default_update,initialize=default_update,respuesta=default_update,*args,**kwargs):
    """
    funcion crear_ventana
    
    Def:
        Esta funcion crea una ventana con los atributos pasados y crea un loop que permite la interacción con la misma

    Args:
        name(str): nombre de la ventana a crear
        
        layout(list): contenido de la ventana a crear

        acciones(function): función que contiene la logistica de la ventana a crear

        update_windows(function): función que actualiza la ventana en caso de ser necesario

        initialize(function):funcion que iniciliaza los datos de la session actual

        respuesta: en caso de que sea la "Pantalla jugar", es la opción correcta de la tarjeta.
        En cualquier otro caso, es la funcion 'dafault'
    """
    tiempo = 900 if name == "Pantalla de Juego"  else None
    initialize(data=sessions)
    window = sg.Window(name,layout,finalize=True, size=(750, 500), element_justification=CENTER)
    loop = True
    while loop:
        event,values = window.read(timeout=tiempo)
        match event:
            case None |sg.WIN_CLOSED:
                break
        loop = acciones(event,values,data=sessions,window=window,respuesta=respuesta)
        update_windows(window,data=sessions)
    window.close()   


def pasar_ventana(window,action):
    window.Hide()
    action()
    window.UnHide()