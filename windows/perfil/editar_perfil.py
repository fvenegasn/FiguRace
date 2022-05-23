import PySimpleGUI as sg
from common.hacer_ventana import crear_ventana
from common.editar_perfil import editar_perfil


"""-------------------------LOGÍSTICA------------------------------"""
def logistica(event,values):
    match event:
        case '-CANCELAR-':
            return False
        case '-ACEPTAR-':
            exito = editar_perfil(values[0],values[1],values[2])
            if exito:
                sg.Popup('Perfil editado con éxito!')
            else:
                sg.Popup('El nick ingresado no existe')
            return False
    return True

"""-------------------------EJECUCIÓN------------------------------"""
def ejecutar():
    layout = [
        [sg.Text('Ingrese su nick', size =(17, 1)), sg.InputText()],
        [sg.Text('Ingrese nuevos datos:')],
        [sg.Text('Edad', size =(17, 1)), sg.InputText()],
        [sg.Text('Género autopercibido', size =(17, 1)), sg.InputText()],
        [sg.Button("Aceptar", key="-ACEPTAR-"), sg.Button("Cancelar", key="-CANCELAR-")]
    ]
    crear_ventana("Editar perfil", layout,logistica)