import PySimpleGUI as sg
from common.hacer_ventana import crear_ventana
from windows import crear_perfil

"""-------------------------LOGÍSTICA------------------------------"""
def logistica(event,values):
    match event:
        case '-CREAR-':
            crear_perfil.ejecutar()
        case '-VOLVER-':
            return False
    return True

"""-------------------------EJECUCIÓN------------------------------"""
def ejecutar():
    layout = [
        [sg.Button("Crear nuevo perfil", key="-CREAR-",font=('Arial',15))],
        [sg.Button("Editar perfil", key="-EDITAR-",font=('Arial',15))],
        [sg.Button("Volver al menú", key="-VOLVER-",font=('Arial',13))],
    ]
    crear_ventana("Perfiles", layout,logistica)