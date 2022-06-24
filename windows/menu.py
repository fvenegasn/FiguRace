import os
import PySimpleGUI as sg
from common.hacer_ventana import crear_ventana,pasar_ventana 
from windows import jugar, como_jugar,configuracion,puntajes
from windows.perfil import perfil
from common.manejo_datos_juego import mostrar_seleccionado,datos_juego_default


"""-------------------------INTERFAZ------------------------------"""
def interfaz():
    ruta_imagen = os.path.join(os.getcwd(),'static','figurace_logo.png')
    
    perfil = [
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
            [sg.Button("Jugar",key="-JUGAR-",font=('Arial',24))],
            [sg.Button("Perfil",key='-PERFIL-',font=('Arial',20))],
            [sg.Button("Puntaje",key='-PUNTAJES-',font=('Arial',20))],
            [sg.Button("Cómo Jugar",key='-COMO-JUGAR-',font=('Arial',20))],
            [sg.Button("Configuración",key='-CONFIGURACION-',font=('Arial',20))],
            [sg.Button("Salir",key='-SALIR-',font=('Arial',13))] 
    ]

    config =[
            [sg.Column(perfil)],
            [sg.Column(dificultad)],
            [sg.Column(dataset)]
    ]

    layout=[
            [sg.Image(filename=ruta_imagen,key='-IMAGEN-')],
            [sg.Column(menu),sg.Column(config)]
        ]
    return layout

"""-------------------------LOGISTICA------------------------------"""
def logica_ventana(event,values,**kwargs):
    window = kwargs['window']
    match event:
        case '-JUGAR-':
            if (mostrar_seleccionado('perfil')=="-None-"):
                sg.Popup('Debe seleccionar un usuario para jugar')
                pasar_ventana(window,perfil.ejecutar)
            else:
                pasar_ventana(window,jugar.ejecutar)
        case '-PUNTAJES-':
            pasar_ventana(window,puntajes.ejecutar)
        case '-PERFIL-':
            pasar_ventana(window,perfil.ejecutar)
        case '-CONFIGURACION-':
            pasar_ventana(window,configuracion.ejecutar)
        case '-COMO-JUGAR-':
            pasar_ventana(window,como_jugar.ejecutar)
        case None | sg.WIN_CLOSED | '-SALIR-':
            return False
    return True

def update_windows(window,**kwargs):
    window['-MOSTRAR_NICK-'].update(mostrar_seleccionado('perfil'))
    window['-MOSTRAR_DIFICULTAD-'].update(mostrar_seleccionado('dificultad'))
    window['-MOSTRAR_DATASET-'].update(mostrar_seleccionado('dataset'))

"""-------------------------EJECUCIÓN------------------------------"""
def ejecutar():
    sg.theme('BrightColors')
    datos_juego_default()
    layout=interfaz()
    crear_ventana("Menú Principal",layout=layout,acciones=logica_ventana,update_windows=update_windows)

