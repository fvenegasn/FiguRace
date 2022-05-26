import PySimpleGUI as sg
from common.hacer_ventana import crear_ventana
from common.verificar_perfil import verificar_perfil,guardar_seleccionado

"""-------------------------LOGÍSTICA------------------------------"""
def logistica(event,values):
    match event:
        case '-CANCELAR-':
            return False
        case '-ACEPTAR-':
            exito = verificar_perfil(values[0],values[1])
            if exito:
                sg.Popup('Perfil seleccionado con éxito!')
                guardar_seleccionado(values[0])
            else:
                sg.Popup('Los datos ingresados son incorrectos :(')
            return False
    return True

"""-------------------------EJECUCIÓN------------------------------"""
def ejecutar():
    layout = [
        [sg.Text('Nick',size =(17, 1)), sg.InputText()],
        [sg.Text('Contraseña', size =(17, 1)), sg.InputText()],
        [sg.Button("Aceptar", key="-ACEPTAR-"), sg.Button("Cancelar", key="-CANCELAR-")]
        ]
    crear_ventana("Seleccionar perfil", layout,logistica)