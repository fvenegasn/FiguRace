import PySimpleGUI as sg
from common.hacer_ventana import crear_ventana
from common.modificar_perfil import editar_perfil
from common.generos import lista_generos
from common.manejo_datos_juego import mostrar_seleccionado
from common.manejo_datos_juego import buscar_usuario

"""-------------------------LOGÍSTICA------------------------------"""
def logistica(event,values,**kwargs):
    match event:
        case '-CANCELAR-':
            return False
        case '-ACEPTAR-':
            exito,caso = editar_perfil(mostrar_seleccionado('perfil'),values[0],values[1])
            if exito:
                sg.Popup('Perfil editado con éxito!')
            else:
                match caso:
                    case 'nick':
                        sg.Popup('No existe el nick')
                    case 'edad inválida'|'genero inválido':
                        sg.Popup(f"Se ingresó {caso}")
            return False
    return True

"""-------------------------EJECUCIÓN------------------------------"""
def ejecutar():
    usuario=buscar_usuario(mostrar_seleccionado('perfil'))
    layout = [[sg.VPush()],
        [
            sg.Text("Figuracer: ",font=('Arial',15)),
            sg.Text(usuario['nick'],key='-MOSTRAR_NICK-',font=('Arial',15),background_color='LavenderBlush3')
        ],
        
        [sg.Text('Ingrese nuevos datos:')],
        
        [sg.Text('Edad:', size =(17, 1)), sg.InputText(usuario['edad'],size=(18,1))],
        
        [sg.Text('Género autopercibido:', size =(17, 1)), sg.Combo(default_value=usuario['genero'],values=lista_generos,size=(16,1))],
        
        [sg.Button("Aceptar", key="-ACEPTAR-"), sg.Button("Cancelar", key="-CANCELAR-")],
        [sg.VPush()]
    ]
    crear_ventana("Editar perfil", layout,logistica)