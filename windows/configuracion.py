import PySimpleGUI as sg
from common.archivo import leer_json_data
from common.paths import ruta_configuracion
from common.hacer_ventana import crear_ventana
from common.manejo_datos_juego import guardar_dato,mostrar_seleccionado
from helpers.guardar_parametros import guardar_parametros
from helpers.transformar_valores import values_to_options
from common.parametros import options
import copy

options_copy = copy.deepcopy(options)

def actualizar_parametros(window,dificultad):
    parametros=leer_json_data(ruta_configuracion)
    
    window['-TIEMPO-'].update(parametros[dificultad]['tiempo_limite'])
    window['-RONDAS-'].update(parametros[dificultad]["cant_rondas"])
    window['-CORRECTAS-'].update(parametros[dificultad]["rta_correcta"])
    window['-INCORRECTAS-'].update(parametros[dificultad]["rta_incorrecta"])
    window['-CANT_CARACT-'].update(parametros[dificultad]["cant_caracteristicas"])

def actualizar_botones(window,dificultad_actual,dataset_actual,data):
    dificultad_anterior=data['dificultad']
    dataset_anterior=data['dataset']
    
    window['-'+dificultad_anterior.upper()+'-'].update(button_color='pink')
    window['-'+dificultad_actual.upper()+'-'].update(button_color='grey')

    window['-'+dataset_anterior.upper()+'-'].update(button_color='pink')
    window['-'+dataset_actual.upper()+'-'].update(button_color='grey')

    data['dificultad']=dificultad_actual
    data['dataset']=dataset_actual

"""-------------------------INTERFAZ-------------------------------"""

def interface():
    dificultad_elegida=mostrar_seleccionado('dificultad')
    dataset_elegido=mostrar_seleccionado('dataset')
    parametros=leer_json_data(ruta_configuracion)
    dificultades=parametros.keys()
    datasets=['Spotify','Lagos','Peliculas']
    
    botones_dataset=[
        [sg.Button(valor,key='-'+valor.upper()+'-',font=('Arial',12),button_color='grey')if valor==dataset_elegido 
        else sg.Button(valor,key='-'+valor.upper()+'-',font=('Arial',12),button_color='pink') 
        for valor in datasets]
        ]
    layout_dataset = [
        sg.Text("Seleccionar dataset: ",font=('Arial',12)),
        sg.Column(botones_dataset)
        ]
    
    botones_dificultad=[
        [sg.Button(valor,key='-'+valor.upper()+'-',font=('Arial',12),button_color='grey')if valor==dificultad_elegida
        else sg.Button(valor,key='-'+valor.upper()+'-',font=('Arial',12),button_color='pink')
            for valor in dificultades]
        ]
    layout_dificultad = [
        sg.Text("Seleccionar dificultad: ",font=('Arial',12)),
        sg.Column(botones_dificultad)
    ]

    layout_parametros = [
        [
            sg.Text('Ingrese el tiempo límite (en segundos)'), 
            sg.InputText(parametros[dificultad_elegida]['tiempo_limite'],key='-TIEMPO-')
        ],
        [
            sg.Text('Ingrese la cantidad de rondas por juego'), 
            sg.InputText(parametros[dificultad_elegida]["cant_rondas"],key='-RONDAS-')
        ],
        [
            sg.Text('Ingrese el puntaje sumado por cada respuesta correcta'), 
            sg.InputText(parametros[dificultad_elegida]["rta_correcta"],key='-CORRECTAS-')
        ],
        [
            sg.Text('Ingrese el puntaje restado por cada respuesta incorrecta'), 
            sg.InputText(parametros[dificultad_elegida]["rta_incorrecta"],key='-INCORRECTAS-')
        ],
        [
            sg.Text('Ingrese la cantidad de características a mostrar'), 
            sg.InputText(parametros[dificultad_elegida]["cant_caracteristicas"],key='-CANT_CARACT-')
        ],
        [
            sg.Button("Modificar dificultad:", key="-MODIFICAR-",font=('Arial',10)),
            sg.Text(dificultad_elegida,key='-MOSTRAR_DIFICULTAD-',font=('Arial',10))
        ]

    ]

    layout = [
        [sg.VPush()],
        [layout_dataset],
        [layout_dificultad],
        [layout_parametros],
        [
            sg.Button('Seleccionar configuración por defecto', key="-DEFAULT-"),
            sg.Button("Volver al menú", key="-VOLVER-",font=('Arial',13))
        ],
        [sg.VPush()]
    ]
    return layout

"""-------------------------LOGÍSTICA------------------------------"""
def logistica(event,values,**kwargs):
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

def update_windows(window,**kwargs):
    data=kwargs['data']
    dificultad_elegida=mostrar_seleccionado('dificultad')
    dataset_elegido=mostrar_seleccionado('dataset')
    window['-MOSTRAR_DIFICULTAD-'].update(dificultad_elegida)
    actualizar_parametros(window,dificultad_elegida)
    actualizar_botones(window,dificultad_elegida,dataset_elegido,data)

"""-------------------------INICIALIZACIÓN  DE CONFIGURACIÓN EN SESIÓN------------------------------"""
def initialize(data):
    data['dificultad']=mostrar_seleccionado('dificultad')
    data['dataset']=mostrar_seleccionado('dataset')

"""-------------------------EJECUCIÓN------------------------------"""
def ejecutar():
    layout=interface()
    crear_ventana("Configuración", layout,acciones=logistica,update_windows=update_windows,initialize=initialize)