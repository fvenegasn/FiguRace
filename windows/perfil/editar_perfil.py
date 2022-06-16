import PySimpleGUI as sg
from common.hacer_ventana import crear_ventana
from common.modificar_perfil import editar_perfil
from common.generos import lista_generos
from common.manejo_datos_juego import mostrar_seleccionado

"""-------------------------LOGÍSTICA------------------------------"""
def logistica(event,values,**kwargs):
    match event:
        case '-CANCELAR-':
            return False
        case '-ACEPTAR-':
            exito = editar_perfil(mostrar_seleccionado('perfil'),values[0],values[1])
            if exito:
                sg.Popup('Perfil editado con éxito!')
            else:
                sg.Popup('Datos ingresados incorrectos')
            return False
    return True

"""-------------------------EJECUCIÓN------------------------------"""
def ejecutar():
    layout = [
        [
            sg.Text("Figuracer: ",font=('Arial',15)),
            sg.Text(
                mostrar_seleccionado('perfil'),key='-MOSTRAR_NICK-',
                font=('Arial',15),background_color='LavenderBlush3'
                )
        ],
        
        [sg.Text('Ingrese nuevos datos:')],
        
        [sg.Text('Edad:', size =(17, 1)), sg.InputText()],
        
        [sg.Text('Género autopercibido:', size =(17, 1)), sg.Combo(values=lista_generos)],
        
        [sg.Button("Aceptar", key="-ACEPTAR-"), sg.Button("Cancelar", key="-CANCELAR-")]
    ]
    crear_ventana("Editar perfil", layout,logistica)