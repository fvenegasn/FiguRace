import os
import PySimpleGUI as sg
from common.hacer_ventana import crear_ventana 
from windows import jugar, como_jugar
from windows.configuration import configuracion
from windows.perfil import perfil
from common.manejo_datos_juego import mostrar_seleccionado
from windows.puntaje import puntajes


"""-------------------------INTERFAZ------------------------------"""
def interfaz():
    ruta_imagen = os.path.join(os.getcwd(),'static','figurace_logo.png')
    ruta_nick = os.path.join(os.getcwd(),'data','txt','perfil_seleccionado.txt')
    perfiles = [
            [
                sg.Text("Figuracer: ",font=('Arial',15)),
                sg.Text(mostrar_seleccionado('perfil'),key='-MOSTRAR_NICK-',font=('Arial',15),background_color='LavenderBlush3')
            ]
        ]
    dificultad = [
            [sg.Text("Dificultad:",font=('Arial',15)),
            sg.Text(mostrar_seleccionado('dificultad'),key='-MOSTRAR_DIFICULTAD-',font=('Arial',15),background_color='LavenderBlush3')
            ]
        ]
    dataset = [
            [sg.Text("Dataset:",font=('Arial',15)),
            sg.Text(mostrar_seleccionado('dataset'),key='-MOSTRAR_DATASET-',font=('Arial',15),background_color='LavenderBlush3')
            ]
        ]
    menu=[
            [sg.Button("Jugar",key="-JUGAR-",font=('Arial',27))],
            [sg.Button("Perfil",key='-PERFIL-',font=('Arial',20))],
            [sg.Button("Puntaje",key='-PUNTAJES-',font=('Arial',20))],
            [sg.Button("Configuración",key='-CONFIGURACION-',font=('Arial',20))],
            [sg.Button("Como Jugar",key='-COMO-JUGAR-',font=('Arial',20))],
            [sg.Button("Actualizar",key='-ACTUALIZAR-',font=('Arial',10))]  
    ]

    config =[
            [sg.Column(perfiles)],
            [sg.Column(dificultad)],
            [sg.Column(dataset)]
    ]

    layout=[
            [sg.Image(filename=ruta_imagen,key='-IMAGEN-')],
            [sg.Column(menu),sg.Column(config)]
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
        
        case '-COMO-JUGAR-':
            como_jugar.ejecutar()

        case '-ACTUALIZAR-':
            ejecutar()
            return False 

        case None | sg.WIN_CLOSED:
            return False
    return True
    

"""-------------------------EJECUCIÓN------------------------------"""
def ejecutar():
    sg.theme('BrightColors')
    layout=interfaz()
    crear_ventana("Menú Principal",layout=layout,acciones=logica_ventana)

