import PySimpleGUI as sg
import json
import os
from common.hacer_ventana import crear_ventana
from common.parametros import options
from windows.configuration import dataset, dificultad, set_parametros


"""-------------------------INTERFAZ-------------------------------"""
def interface():
    layout = [
        [sg.Button("DIFICULTAD", key="-DIFICULTAD-",font=('Arial',15))],
        [sg.Button("PARAMETROS", key="-PARAMETROS-",font=('Arial',15))],
        [sg.Button("DATASET", key="-DATASET-",font=('Arial',15))],
        [sg.Button("Volver al menú", key="-VOLVER-",font=('Arial',13))],
    ]
    return layout

"""-------------------------LOGÍSTICA------------------------------"""
def logistica(event,values):

    match event:
        case '-DIFICULTAD-':
            dificultad.ejecutar()
        case '-PARAMETROS-':
            set_parametros.ejecutar()
        case '-DATASET-':
            dataset.ejecutar()
        case '-VOLVER-':
            return False
    return True

"""-------------------------EJECUCIÓN------------------------------"""
def ejecutar():
    layout=interface()
    crear_ventana("Configuración", layout,acciones=logistica)