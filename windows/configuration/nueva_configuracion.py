from platform import architecture
import PySimpleGUI as sg
import json
import os
from common.hacer_ventana import crear_ventana
from common.parametros import options
from helpers.transformar_valores import values_to_options
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
    archivo = open (os.path.join(os.getcwd(), 'data','json',"configuracion.json"), "w", encoding="UTF-8")
    difficulty = "Media" #Dificultad por defecto
    chosen_dataset = "Lagos Argentina" #Dataset por defecto
    match event:
        case '-DIFICULTAD-':
            difficulty = dificultad.ejecutar()
        case '-PARAMETROS-':
            parametros = set_parametros.ejecutar()
            if options != parametros:
                values_to_options (options, parametros, difficulty)
            json.dump (options, archivo, indent=4)
        case '-DATASET-':
            chosen_dataset = dataset.ejecutar()
            print (chosen_dataset)
        case '-VOLVER-':
            json.dump (options, archivo, indent=4)
            return False
    return True

"""-------------------------EJECUCIÓN------------------------------"""
def ejecutar():
    layout=interface()
    crear_ventana("Configuración", layout,acciones=logistica)