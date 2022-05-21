from sre_parse import expand_template
import PySimpleGUI as sg
from common.hacer_ventana import crear_ventana
import os
from puntajes import abrir_puntajes

#from abrir_menu import abrir_menu
#from juego import abrir_juego


ruta_imagen = os.path.join(os.getcwd(),'static','imagenes','figurace_logo.png')
menu = [
        [sg.Button("Jugar",key="-JUGAR-",font=('Arial',27))],
        [sg.Button("Configuración",key='-CONFIGURACION-',font=('Arial',20))],
        [sg.Button("Puntaje",key='-PUNTAJES-',font=('Arial',20))],
        [sg.Button("Perfil",key='-PERFIL-',font=('Arial',20))],
    ]
layout=[
        #[sg.Image(ruta_imagen)],
        [sg.Column(menu)]#,sg.Column(perfiles)],
        #[dificultad]
    ]


def logica_ventana(event,values):#,window):

    match event:
        case '-JUGAR-':
            print("JUGAR")
            #crear_ventana(event,values)
        case '-PUNTAJES-':
            #print("PUNTAJES")
            abrir_puntajes()
        case '-PERFIL-':
            print("PERFIL")
            #renderizar_ventana
        case '-CONFIGURACION-':
            print("CONFIGURACION")
            #renderizar puntajes
        case sg.WIN_CLOSED:
            return False
    return True
    

def ejecutar():
    sg.theme('BrightColors')
    crear_ventana("Menú Principal",layout=layout,acciones=logica_ventana)
    
# WHILE TRUE:
    #    CURRENT_WINDOW, EVENT, VALUES = SG.READ_ALL_WINDOWS()
    #    IF EVENT == SG.WIN_CLOSED:
    #        CURRENT_WINDOW.CLOSE()
    #         BREAK
    #     ELIF EVENT == '-JUGAR-':
    #         ABRIR_JUEGO()
    #         CURRENT_WINDOW.CLOSE()
    #     ELIF EVENT == '-PUNTAJES-':
    #         ABRIR_PUNTAJES()
    #         CURRENT_WINDOW.CLOSE()
    #     ELIF EVENT == '-VOLVER-':
    #         ABRIR_MENU()
    #         CURRENT_WINDOW.CLOSE()
