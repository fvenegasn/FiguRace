import PySimpleGUI as sg
from common.hacer_ventana import crear_ventana
import os
from static import explicacion_juego 
    

"""-------------------------INTERFAZ-------------------------------"""
def interface():
    ruta_imagen = os.path.join(os.getcwd(),'static','figurace_logo.png')
    
    about_general = [
            [sg.Text("Jugar: ",font=('Arial',14))],
            [sg.Text(explicacion_juego.play_button,key='-PLAY-',font=('Arial',12))],
            [sg.Text("Perfil: ",font=('Arial',14))],
            [sg.Text(explicacion_juego.profile_button,key='-PROFILE-',font=('Arial',12))],
            [sg.Text("Puntajes: ",font=('Arial',14))],
            [sg.Text(explicacion_juego.score_button,key='-SCORE-',font=('Arial',12))],
            [sg.Text("Configuración: ",font=('Arial',14))],
            [sg.Text(explicacion_juego.config_button,key='-CONFIG-',font=('Arial',12))]
    ]

    layout=[
            [sg.Image(filename=ruta_imagen,key='-IMAGEN-', size=(336,137))],
            [sg.Column(about_general, scrollable=True,  vertical_scroll_only=True, size=(750,300))],
            [sg.Button("Volver al menú", key="-VOLVER-",font=('Arial',13))],
        ]
    return layout

"""-------------------------LOGÍSTICA------------------------------"""
def logistica(event,values,**kwargs):
    match event:
        case '-VOLVER-':
            return False
    return True


"""-------------------------EJECUCIÓN------------------------------"""
def ejecutar():
    layout=interface()
    crear_ventana("Cómo Jugar", layout,acciones=logistica)