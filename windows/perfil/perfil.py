import PySimpleGUI as sg
from common.hacer_ventana import crear_ventana
from windows.perfil import crear_perfil,editar_perfil, seleccionar_perfil

"""-------------------------LOGÍSTICA------------------------------"""
def logistica(event,values):
    match event:
        case '-SELECCIONAR-':
            seleccionar_perfil.ejecutar()
        case '-CREAR-':
            crear_perfil.ejecutar()
        case '-EDITAR-':
            editar_perfil.ejecutar()
        case '-VOLVER-':
            return False
    return True

"""-------------------------EJECUCIÓN------------------------------"""
def ejecutar():
    layout = [
        [sg.Button("Seleccionar perfil", key="-SELECCIONAR-",font=('Arial',15))],
        [sg.Button("Crear nuevo perfil", key="-CREAR-",font=('Arial',15))],
        [sg.Button("Editar perfil", key="-EDITAR-",font=('Arial',15))],
        [sg.Button("Volver al menú", key="-VOLVER-",font=('Arial',13))],
    ]
    crear_ventana("Perfiles", layout,logistica)