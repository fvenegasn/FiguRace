import PySimpleGUI as sg
from common.hacer_ventana import crear_ventana
from common.manejo_datos_juego import guardar_dato

"""-------------------------INTERFAZ-------------------------------"""
def interface():
    layout = [
        [sg.Button("Spotify", key="-SPOTIFY-",font=('Arial',15))],
        [sg.Button("Lagos Argentina", key="-LAGOS ARGENTINA-",font=('Arial',15))],
        [sg.Button("Películas", key="-PELÍCULAS-",font=('Arial',15))],
        [sg.Button("Volver al menú", key="-VOLVER-",font=('Arial',13))],
    ]
    return layout

"""-------------------------LOGÍSTICA------------------------------"""
def logistica(event,values):
    match event:
        case '-SPOTIFY-'|'-LAGOS ARGENTINA-'| '-PELÍCULAS-':
            guardar_dato(event.replace('-','').title(),'dataset')
            return False
        case '-VOLVER-':
            return False
    return True

"""-------------------------EJECUCIÓN------------------------------"""
def ejecutar():
    layout=interface()
    crear_ventana("Selección de Dataset", layout,acciones=logistica)
