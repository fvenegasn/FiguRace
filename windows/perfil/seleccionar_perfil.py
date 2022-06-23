import PySimpleGUI as sg
from common.hacer_ventana import crear_ventana
from common.verificar_perfil import verificar_perfil
from common.manejo_datos_juego import guardar_dato

"""-------------------------LOGÍSTICA------------------------------"""
def logistica(event,values,**kwargs):
    load_user=False
    match event:
        case '-CANCELAR-':
            return False
        case '-ACEPTAR-':
            exito = verificar_perfil(values[0],values[1])
            if exito:
                sg.Popup('Perfil seleccionado con éxito!')
                guardar_dato(values[0],'perfil')
                load_user=True
            else:
                sg.Popup('Los datos ingresados son incorrectos :(')
            return False
    return True,load_user

"""-------------------------EJECUCIÓN------------------------------"""
def ejecutar():
    layout = [
        [sg.VPush()],
        [sg.Text('Nick',size =(17, 1)), sg.InputText()],
        [sg.Text('Contraseña', size =(17, 1)), sg.InputText(password_char="*")],
        [sg.Button("Aceptar", key="-ACEPTAR-"), sg.Button("Cancelar", key="-CANCELAR-")],
        [sg.VPush()]
        ]
    crear_ventana("Seleccionar perfil", layout,logistica)