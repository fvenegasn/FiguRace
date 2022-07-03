import PySimpleGUI as sg
from common.hacer_ventana import crear_ventana
from common.guardar_perfil import guardar_perfil
from common.generos import lista_generos
from common.manejo_datos_juego import guardar_dato


"""-------------------------LOGÍSTICA------------------------------"""
def logistica(event,values,**kwargs):
    match event:
        case '-CANCELAR-':
            return False
        case '-CREAR-':
            exito,caso = guardar_perfil(values[0],values[1],values[2],values[3])
            if exito:
                sg.Popup('Perfil creado con éxito!')
                guardar_dato(values[0],'perfil')
                load_user=True
            else:
                match caso:
                    case 'nick':
                        sg.Popup('El nick ingresado ya existe')
                    case 'edad inválida'|'nick inválido'|'genero inválido':
                        sg.Popup(f"Se ingresó {caso}")
                    case 'contraseña inválida':
                        sg.Popup('Se debe crear una contraseña')
            return False
    return True,load_user

"""-------------------------EJECUCIÓN------------------------------"""
def ejecutar():
    layout = [
        [sg.VPush()],

        [sg.Text('Ingrese los siguientes datos:')],
        
        [sg.Text('Nick', size =(17, 1)), sg.InputText(size=(18,1))],
        
        [sg.Text('Edad', size =(17, 1)), sg.InputText(size=(18,1))],
        
        [sg.Text('Género autopercibido', size =(17, 1)), sg.Combo(values=lista_generos,size=(16,1))],
        
        [sg.Text('Contraseña', size =(17, 1)), sg.InputText(password_char="*",size=(18,1))],
        
        [sg.Button("Crear", key="-CREAR-"), sg.Button("Cancelar", key="-CANCELAR-")],
        [sg.VPush()]
    ]
    crear_ventana("Crear perfil", layout,logistica)