import PySimpleGUI as sg
from common.hacer_ventana import crear_ventana

"""-------------------------INTERFAZ-------------------------------"""
def interface():
    layout = [
        [sg.Button("Spotify", key="-SPOTIFY-",font=('Arial',15))],
        [sg.Button("Lagos Argentina", key="-LAGOS-",font=('Arial',15))],
        [sg.Button("Películas", key="-PELIS-",font=('Arial',15))],
        [sg.Button("Volver al menú", key="-VOLVER-",font=('Arial',13))],
    ]
    return layout

"""-------------------------LOGÍSTICA------------------------------"""
def logistica(event,values):
    global chosen_dataset
    chosen_dataset = "Lagos Argentina"
    match event:
        case '-SPOTIFY-':
            chosen_dataset = "Spotify"
            return False
        case '-LAGOS-':
            chosen_dataset = "Lagos Argentina"
            return False
        case '-PELIS-':
            chosen_dataset = "Películas"
            return False
        case '-VOLVER-':
            return False
    return True

"""-------------------------EJECUCIÓN------------------------------"""
def ejecutar():
    layout=interface()
    crear_ventana("Selección de Dataset", layout,acciones=logistica)
    return chosen_dataset