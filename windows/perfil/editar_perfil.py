import PySimpleGUI as sg
from common.hacer_ventana import crear_ventana
from common.modificar_perfil import editar_perfil
from common.generos import lista_generos

"""-------------------------LOGÍSTICA------------------------------"""
def logistica(event,values):
    match event:
        case '-CANCELAR-':
            return False
        case '-ACEPTAR-':
            exito = editar_perfil(values[0],values[1],values[2],values[3])
            if exito:
                sg.Popup('Perfil editado con éxito!')
            else:
                sg.Popup('El nick ingresado no existe o no se ingresó una edad válida')
            return False
    return True

"""-------------------------EJECUCIÓN------------------------------"""
def ejecutar():
    layout = [
        [
            sg.Text('Ingrese su nick', size =(17, 1)), 
            sg.InputText()
            ],
        [
            sg.Text('Ingrese nuevos datos:')
            ],
        [
            sg.Text('Edad', size =(17, 1)), 
            sg.InputText()
            ],
        [
            sg.Text('Género autopercibido', size =(17, 1)), 
            sg.Combo(values=lista_generos)
            ],
        [
            sg.Text('Contraseña', size =(17, 1)), sg.InputText()
            ],
        [
            sg.Button("Aceptar", key="-ACEPTAR-"), 
            sg.Button("Cancelar", key="-CANCELAR-")
            ]
    ]
    crear_ventana("Editar perfil", layout,logistica)