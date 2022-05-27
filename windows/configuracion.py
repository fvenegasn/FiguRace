import PySimpleGUI as sg
import json
import os
from common.parametros import options
from helpers.transformar_valores import values_to_options

#Pantalla de selección de dificultad
def primary_configuration():
    layout = [
        [sg.Button("Facil", size=(10, 1))],
        [sg.Button("Media", size=(10, 1))],
        [sg.Button("Dificil", size=(10, 1))],
    ]
    
    return sg.Window("Selección de dificultad", layout, margins=(100, 50), finalize=True)

#Pantalla de configuración de parámetros    
def secondary_configuration():
    layout = [ 
        [sg.Text('Ingrese el tiempo límite (en segundos)'), sg.InputText()],
        [sg.Text('Ingrese la cantidad de rondas por juego'), sg.InputText()],
        [sg.Text('Ingrese el puntaje sumado por cada respuesta correcta'), sg.InputText()],
        [sg.Text('Ingrese el puntaje sumado por cada respuesta incorrecta'), sg.InputText()],
        [sg.Text('Ingrese la cantidad de características a mostrar'), sg.InputText()],
        [sg.Button('Continuar'), sg.Button('Cancelar')] 
    ]

    return sg.Window("Selección de opciones", layout, margins=(100, 50), finalize=True)

def ejecutar():
    archivo = open (os.path.join(os.getcwd(), 'data','json',"configuracion.json"), "w", encoding="UTF-8")
    window = primary_configuration()

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            window.close() #-> si se descomenta se rompe todo.
            break
        elif event == "Facil" or event == "Media" or event == "Dificil":
            #entrar en la dificultad ingresada y llamar a segunda ventana
            difficulty = event
            window.close()
            window = secondary_configuration()
        elif event == "Continuar" or event == "Cancelar":
            #procesar pantalla con parametros
            values_to_options(options, values, difficulty)
            window.close()

    json.dump(options, archivo)
    archivo.close