import PySimpleGUI as sg
from common.hacer_ventana import crear_ventana
from common.manejo_datos_juego import guardar_dato
from common.manejo_datos_juego import mostrar_seleccionado
from common.guardar_parametros import guardar_parametros
from helpers.transformar_valores import values_to_options
from common.parametros import options
import copy
options_copy = copy.deepcopy(options)


"""-------------------------INTERFAZ-------------------------------"""
def interface():
    layout_dataset = [
            sg.Text("Seleccionar data set: ",font=('Arial',12)),
            sg.Button("Spotify", key="-SPOTIFY-",font=('Arial',12)),
            sg.Button("Lagos", key="-LAGOS-",font=('Arial',12)),
            sg.Button("Peliculas", key="-PELICULAS-",font=('Arial',12))
        ]
    

    layout_dificultad = [
        sg.Text("Seleccionar dificultad: ",font=('Arial',12)),
        sg.Button("FACIL", key="-FACIL-",font=('Arial',12)),
        sg.Button("MEDIA", key="-MEDIA-",font=('Arial',12)),
        sg.Button("DIFICIL", key="-DIFICIL-",font=('Arial',12))
    ]

    layout_paremetros = [
        [sg.Text('Ingrese el tiempo límite (en segundos)'), sg.InputText()],
        
        [sg.Text('Ingrese la cantidad de rondas por juego'), sg.InputText()],
        
        [sg.Text('Ingrese el puntaje sumado por cada respuesta correcta'), sg.InputText()],
        
        [sg.Text('Ingrese el puntaje sumado por cada respuesta incorrecta'), sg.InputText()],
        
        [sg.Text('Ingrese la cantidad de características a mostrar'), sg.InputText()],

        [
            sg.Button("Modificar dificultad:", key="-MODIFICAR-",font=('Arial',10)),
            sg.Text(mostrar_seleccionado('dificultad'),key='-MOSTRAR_DIFICULTAD-',font=('Arial',10))
        ]

    ]


    layout = [
        [layout_dataset],
        [layout_dificultad],
        [layout_paremetros],
        [
            sg.Button('Seleccionar configuración por defecto', key="-DEFAULT-"),
            sg.Button("Volver al menú", key="-VOLVER-",font=('Arial',13))
        ]
    ]
    return layout

"""-------------------------LOGÍSTICA------------------------------"""
def logistica(event,values):
    evento = event.replace('-','')
    match event:
        
        case '-FACIL-'|'-MEDIA-'|'-DIFICIL-':
            guardar_dato(evento.title(),'dificultad')
            sg.Popup('Dificultad ' + evento + ' seleccionada')
        
        case '-MODIFICAR-':
            exito = values_to_options(options_copy, values, mostrar_seleccionado('dificultad'))
            if exito:
                guardar_parametros(options_copy)
                sg.Popup('Dificultad ' + mostrar_seleccionado('dificultad') + ' modificada con exito')
            else:
                sg.Popup('Ingrese datos válidos')

        case '-DEFAULT-':
            guardar_parametros(options)
            sg.Popup('Se seleccionó la configuración de dificultad por defecto')
        
        case '-SPOTIFY-'|'-LAGOS-'| '-PELICULAS-':
            guardar_dato(evento.title(),'dataset')
            sg.Popup('Dataset ' + evento + ' seleccionado')
        
        case '-VOLVER-':
            return False
    return True

def update_windows(window):
    window['-MOSTRAR_DIFICULTAD-'].update(mostrar_seleccionado('dificultad'))

"""-------------------------EJECUCIÓN------------------------------"""
def ejecutar():
    layout=interface()
    crear_ventana("Configuración", layout,acciones=logistica,update_windows=update_windows)