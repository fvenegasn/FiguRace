#from sre_parse import expand_template
import os
import PySimpleGUI as sg
from common.hacer_ventana import crear_ventana #renderizar_ventana

from windows import jugar, puntajes, configuracion
from windows.perfil import perfil

#from abrir_menu import abrir_menu
#from juego import abrir_juego

"""-------------------------INTERFAZ------------------------------"""
def interfaz():
    ruta_imagen = os.path.join(os.getcwd(),'static','figurace_logo.png')
  
    perfiles_lista = ['Usuario 1','Usuario 2','Usuario 3','Usuario 4']
    perfiles = [
            [sg.Text("Perfiles",font=('Arial',15)),
            sg.Combo(values=perfiles_lista,size=(10,10))]
        ]
    dificultad = [
            [sg.Text("Dificultades",font=('Arial',15)),
            sg.Combo(values=["Fácil","Media","Difícil"],size=(10,10))
            ]
        ]
    menu=[
            [sg.Button("Jugar",key="-JUGAR-",font=('Arial',27))],
            [sg.Button("Configuración",key='-CONFIGURACION-',font=('Arial',20))],
            [sg.Button("Puntaje",key='-PUNTAJES-',font=('Arial',20))],
            [sg.Button("Editar Perfil",key='-PERFIL-',font=('Arial',20))],
    ]

    layout=[
            [sg.Image(filename=ruta_imagen,key='-IMAGEN-')],
            [sg.Column(menu)],
            [sg.Column(perfiles),sg.Column(dificultad)]
        ]
    return layout


"""-------------------------LOGISTICA------------------------------"""
def logica_ventana(event,values):

    match event:
        case '-JUGAR-':
            jugar.ejecutar()

        case '-PUNTAJES-':
            puntajes.ejecutar()

        case '-PERFIL-':
            perfil.ejecutar()

        case '-CONFIGURACION-':
            configuracion.ejecutar()

        case sg.WIN_CLOSED:
            return False
    return True
    

"""-------------------------EJECUCIÓN------------------------------"""
def ejecutar():
    sg.theme('BrightColors')
    layout=interfaz()
    crear_ventana("Menú Principal",layout=layout,acciones=logica_ventana)

