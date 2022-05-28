import PySimpleGUI as sg
from common.hacer_ventana import crear_ventana

"""-------------------------INTERFAZ-------------------------------"""
def interface():
    layout = [
        [sg.Button("FACIL", key="-FACIL-",font=('Arial',15))],
        [sg.Button("MEDIA", key="-MEDIA-",font=('Arial',15))],
        [sg.Button("DIFICIL", key="-DIFICIL-",font=('Arial',15))],
        [sg.Button("Volver al menú", key="-VOLVER-",font=('Arial',13))],
    ]
    return layout

"""-------------------------LOGÍSTICA------------------------------"""
def logistica(event,values):
    global difficulty
    difficulty = "Media"
    match event:
        case '-FACIL-':
            difficulty = "Facil"
            return False
        case '-MEDIA-':
            difficulty = "Media"
            return False
        case '-DIFICIL-':
            difficulty = "Dificil"
            return False
        case '-VOLVER-':
            return False
    return True


"""-------------------------EJECUCIÓN------------------------------"""
def ejecutar():
    layout=interface()
    crear_ventana("Selección de dificultad", layout,acciones=logistica)
    return difficulty