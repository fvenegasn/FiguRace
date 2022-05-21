import PySimpleGUI as sg
from common.hacer_ventana import crear_ventana


"""-------------------------LOGÍSTICA------------------------------"""
def logistica(event,values):
    match event:
        case '-VOLVER-':
            return False
    return True

"""-------------------------EJECUCIÓN------------------------------"""
def ejecutar():
    layout = [
        [sg.Text("Pantalla de juego",font=('Arial',15))],
        [sg.Button("Volver al menú", key="-VOLVER-",font=('Arial',15))],
    ]
    crear_ventana("Pantalla de Juego", layout,logistica)
