import json
import os
import PySimpleGUI as sg
from common.parametros import options
from common.hacer_ventana import crear_ventana
from helpers.transformar_valores import values_to_options

archivo = open (os.path.join(os.getcwd(), 'data','json',"configuracion.json"), "w", encoding="UTF-8")

"""-------------------------INTERFAZ-------------------------------"""
def interface():
    layout = [ 
        [sg.Text('Ingrese el tiempo límite (en segundos)'), sg.InputText()],
        [sg.Text('Ingrese la cantidad de rondas por juego'), sg.InputText()],
        [sg.Text('Ingrese el puntaje sumado por cada respuesta correcta'), sg.InputText()],
        [sg.Text('Ingrese el puntaje sumado por cada respuesta incorrecta'), sg.InputText()],
        [sg.Text('Ingrese la cantidad de características a mostrar'), sg.InputText()],
        [sg.Button('Continuar', key="-CONTINUAR-"), sg.Button('Cancelar', key="-CANCELAR-")] 
    ]
    return layout

"""-------------------------LOGÍSTICA------------------------------"""
def logistica(event, values):
    global dict_values
    match event:
        case '-CONTINUAR-':
            dict_values = values
            return False
        case '-CANCELAR-':
            dict_values = options
            return False
    return True


"""-------------------------EJECUCIÓN------------------------------"""
def ejecutar():
    layout=interface()
    crear_ventana("Selección de dificultad", layout,acciones=logistica)
    return dict_values