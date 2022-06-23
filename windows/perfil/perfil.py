import PySimpleGUI as sg
from common.hacer_ventana import crear_ventana,pasar_ventana
from windows.perfil import crear_perfil,editar_perfil, seleccionar_perfil
from common.manejo_datos_juego import mostrar_seleccionado

"""-------------------------LOGÍSTICA------------------------------"""
def logistica(event,values,**kwargs):
    window = kwargs['window']
    match event:
        case '-SELECCIONAR-':
            pasar_ventana(window,seleccionar_perfil.ejecutar)
        case '-CREAR-':
            pasar_ventana(window,crear_perfil.ejecutar)
        case '-EDITAR-':
            if (mostrar_seleccionado('perfil')=="-None-"):
                sg.Popup('Seleccione usuario')
            else:
                pasar_ventana(window,editar_perfil.ejecutar)
        case '-VOLVER-':
            return False
    return True

"""-------------------------EJECUCIÓN------------------------------"""
def ejecutar():
    layout = [
        [sg.VPush()],
        [sg.Button("Seleccionar perfil", key="-SELECCIONAR-",font=('Arial',15))],
        [sg.Button("Crear nuevo perfil", key="-CREAR-",font=('Arial',15))],
        [sg.Button("Editar perfil", key="-EDITAR-",font=('Arial',15))],
        [sg.Button("Volver al menú", key="-VOLVER-",font=('Arial',13))],
        [sg.VPush()]
    ]
    crear_ventana("Perfiles", layout,logistica)