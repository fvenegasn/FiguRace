import PySimpleGUI as sg
from common.hacer_ventana import crear_ventana
from common.guardar_perfil import guardar_perfil
from common.generos import lista_generos
from common.manejo_datos_juego import guardar_dato


"""-------------------------LOGÍSTICA------------------------------"""
def logistica(event,values):
    match event:
        case '-CANCELAR-':
            return False
        case '-CREAR-':
            exito = guardar_perfil(values[0],values[1],values[2],values[3])
            if exito:
                sg.Popup('Perfil creado con éxito!')
                guardar_dato(values[0],'perfil')
                load_user=True
            else:
                sg.Popup('El nick ingresado ya existe o no se ingresó una edad válida')
            return False
    return True,load_user

"""-------------------------EJECUCIÓN------------------------------"""
def ejecutar():
    layout = [
        [sg.Text('Ingrese los siguientes datos:')],
        
        [sg.Text('Nick', size =(17, 1)), sg.InputText()],
        
        [sg.Text('Edad', size =(17, 1)), sg.InputText()],
        
        [sg.Text('Género autopercibido', size =(17, 1)), sg.Combo(values=lista_generos)],
        
        [sg.Text('Contraseña', size =(17, 1)), sg.InputText(password_char="*")],
        
        [sg.Button("Crear", key="-CREAR-"), sg.Button("Cancelar", key="-CANCELAR-")]
    ]
    crear_ventana("Crear perfil", layout,logistica)