import PySimpleGUI as sg
import json
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

#Esta función devolverá la dificultad elegida por el usuario a efectos de modificar los valores de la configuración correctos
def check_difficulty (event):
    if event == "Facil":
        return "Facil"
    elif event == "Media":
        return "Media"
    elif event == "Dificultad":
        return "Dificil"
    
#Esta función pasa los valores ingresados en pantalla por el usuario a la configuración del juego
def values_to_options(options, values, difficulty):
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
    archivo = open ("configuracion.txt", "w", encoding="UTF-8")
    window = primary_configuration()

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            window.close() #-> si se descomenta se rompe todo.
            break
        elif event == "Facil" or event == "Media" or event == "Dificil":
            #entrar en la dificultad ingresada y llamar a segunda ventana
            difficulty = check_difficulty(event)
            window.close()
            window = secondary_configuration()
        elif event == "Continuar" or event == "Cancelar":
            #procesar pantalla con parametros
            values_to_options(options, values, difficulty)
            window.close()

    json.dump(options, archivo)
    archivo.close