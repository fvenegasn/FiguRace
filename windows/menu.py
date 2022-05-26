#from sre_parse import expand_template
import os
import PySimpleGUI as sg
from common.hacer_ventana import crear_ventana #renderizar_ventana

from windows import jugar, puntajes, configuracion
from windows.perfil import perfil
from common.verificar_perfil import mostrar_seleccionado

"""-------------------------INTERFAZ------------------------------"""
def interfaz():
    ruta_imagen = os.path.join(os.getcwd(),'static','figurace_logo.png')
    ruta_nick = os.path.join(os.getcwd(),'data','txt','perfil_seleccionado.txt')
    perfiles = [
            [
                sg.Text("Figuracer: ",font=('Arial',15)),
                sg.Text(mostrar_seleccionado(ruta_nick),key='-MOSTRAR_NICK-',font=('Arial',15))
            ]
        ]
    dificultad = [
            [sg.Text("Dificultades",font=('Arial',15)),
            sg.Combo(values=["Fácil","Media","Difícil"],size=(10,10))
            ]
        ]
    menu=[
            [sg.Button("Jugar",key="-JUGAR-",font=('Arial',27))],
            [sg.Button("Perfil",key='-PERFIL-',font=('Arial',20))],
            [sg.Button("Puntaje",key='-PUNTAJES-',font=('Arial',20))],
            [sg.Button("Configuración",key='-CONFIGURACION-',font=('Arial',20))],
            [sg.Button("Actualizar",key='-ACTUALIZAR-',font=('Arial',10))]
            
    ]

    layout=[
            [sg.Image(filename=ruta_imagen,key='-IMAGEN-')],
            [sg.Column(menu)],
            [sg.Column(perfiles)],
            [sg.Column(dificultad)]
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
        
        case '-ACTUALIZAR-':
            ejecutar()
            return False 
        case sg.WIN_CLOSED:
            return False
    return True
    

"""-------------------------EJECUCIÓN------------------------------"""
def ejecutar():
    sg.theme('BrightColors')
    layout=interfaz()
    crear_ventana("Menú Principal",layout=layout,acciones=logica_ventana)

