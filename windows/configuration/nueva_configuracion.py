from this import d
import PySimpleGUI as sg
import json
import os
from common.hacer_ventana import crear_ventana
from common.parametros import options
from helpers.transformar_valores import values_to_options
from windows.configuration import dataset, dificultad, set_parametros
from common.manejo_datos_juego import guardar_dato
import copy
options_copy = copy.deepcopy(options)

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
            difficulty = dificultad.ejecutar()
            guardar_dato(difficulty,'dificultad')
        case '-PARAMETROS-':
            parametros, dificultad_modif = set_parametros.ejecutar()
            if parametros != None:
                ruta = os.path.join(os.getcwd(), 'data','json',"configuracion.json")
                with open (ruta, "w", encoding="UTF-8") as archivo:
                    values_to_options (options_copy, parametros, dificultad_modif)
                    json.dump (options_copy, archivo, indent=4)
        case '-DATASET-':
            chosen_dataset = dataset.ejecutar()
            guardar_dato(chosen_dataset,'dataset')
        case '-VOLVER-':
            return False
    return True

"""-------------------------EJECUCIÓN------------------------------"""
def ejecutar():
    layout=interface()
    crear_ventana("Configuración", layout,acciones=logistica)