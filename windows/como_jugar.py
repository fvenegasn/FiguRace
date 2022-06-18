import PySimpleGUI as sg
from common.hacer_ventana import crear_ventana
import os
from static import explicacion_juego 
    

"""-------------------------INTERFAZ-------------------------------"""
def interface():
    ruta_imagen = os.path.join(os.getcwd(),'static','figurace_logo.png')
    
    about_jugar = [
            [
                sg.Text("Jugar: ",font=('Arial',14)),
                sg.Text(explicacion_juego.play_button,key='-PLAY-',font=('Arial',12))
            ]
        ]
    about_perfil = [
            [
                sg.Text("Perfil: ",font=('Arial',14)),
                sg.Text(explicacion_juego.profile_button,key='-PROFILE-',font=('Arial',12))
            ]
        ]
    about_puntajes = [
            [
                sg.Text("Puntajes: ",font=('Arial',14)),
                sg.Text(explicacion_juego.score_button,key='-SCORE-',font=('Arial',12))
            ]
        ]
    about_config = [
            [
                sg.Text("Configuración: ",font=('Arial',14)),
                sg.Text(explicacion_juego.config_button,key='-CONFIG-',font=('Arial',12))
            ]
        ]

    layout=[
            [sg.Image(filename=ruta_imagen,key='-IMAGEN-')],
            [sg.Column(about_jugar, scrollable=True,  vertical_scroll_only=True)],
            [sg.Column(about_perfil, scrollable=True,  vertical_scroll_only=True)],
            [sg.Column(about_puntajes, scrollable=True,  vertical_scroll_only=True)],
            [sg.Column(about_config, scrollable=True,  vertical_scroll_only=True)],
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