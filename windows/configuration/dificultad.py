import PySimpleGUI as sg
from common.hacer_ventana import crear_ventana
from common.manejo_datos_juego import guardar_dato

"""-------------------------INTERFAZ-------------------------------"""
def interface():
    layout = [
        [sg.Button("FACIL", key="-FACIL-",font=('Arial',15))],
        [sg.Button("MEDIA", key="-MEDIA-",font=('Arial',15))],
        [sg.Button("DIFICIL", key="-DIFICIL-",font=('Arial',15))],
        [sg.Button("Volver", key="-VOLVER-",font=('Arial',13))],
    ]
    return layout

"""-------------------------LOGÍSTICA------------------------------"""
def logistica(event,values):

    match event:
        case '-FACIL-':
            guardar_dato("Facil",'dificultad')
            return False
        case '-MEDIA-':
            guardar_dato("Media",'dificultad')
            return False
        case '-DIFICIL-':
            guardar_dato("Dificil",'dificultad')
            return False
        case '-VOLVER-':
            return False
    return True


"""-------------------------EJECUCIÓN------------------------------"""
def ejecutar():
    layout=interface()
    crear_ventana("Selección de dificultad", layout,acciones=logistica)
