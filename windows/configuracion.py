import PySimpleGUI as sg
import json
import os
from common.validar_numeros import validate_integer

#El juego tiene, por default, una configuración determinada para cada dificultad
options = {
    "Facil":{"tiempo_limite" : 60,
    "cant_rondas": 10,
    "rta_correcta" : 1, 
    "rta_incorrecta" : 0, 
    "cant_caracteristicas" : 5
    },

    "Media":{"tiempo_limite" : 30,
    "cant_rondas": 10,
    "rta_correcta" : 1, 
    "rta_incorrecta" : 0.5, 
    "cant_caracteristicas" : 3
    },

    "Dificil":{"tiempo_limite" : 15,
    "cant_rondas": 10,
    "rta_correcta" : 1, 
    "rta_incorrecta" : 1, 
    "cant_caracteristicas" : 2
    }
}
    
#Esta función pasa los valores ingresados en pantalla por el usuario a la configuración del juego
def values_to_options(options:dict, values:dict, difficulty:str) -> None:
    """
    función 'values_to_options'

    Def:
        Modifica el diccionario con los parámetros de configuración predeterminado con los valores
        ingresados por el usuario en pantalla.
    
    Args:
        - options (dict): Diccionario que contiene los parámetros de juego para cada dificultad
        - values (dict): Diccionario que contiene los parámetros de juego ingresado por el usuario en pantalla
        - difficulty (str): String que contiene la dificultad elegida por el usuario en pantalla
    """
    x = 0
    dicc_aux = options[difficulty]
    for elem in dicc_aux:
        if (values[x] != "" and validate_integer(values[x])):
            dicc_aux[elem] = values[x]
        x = x + 1

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