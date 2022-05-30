import PySimpleGUI as sg
from common.hacer_ventana import crear_ventana
from common.guardar_parametros import guardar_parametros
from helpers.transformar_valores import values_to_options
from common.parametros import options
import copy
options_copy = copy.deepcopy(options)

"""-------------------------INTERFAZ-------------------------------"""
def interface():
    layout = [
        [sg.Text('Ingrese el tiempo límite (en segundos)'), sg.InputText()],
        [sg.Text('Ingrese la cantidad de rondas por juego'), sg.InputText()],
        [sg.Text('Ingrese el puntaje sumado por cada respuesta correcta'), sg.InputText()],
        [sg.Text('Ingrese el puntaje sumado por cada respuesta incorrecta'), sg.InputText()],
        [sg.Text('Ingrese la cantidad de características a mostrar'), sg.InputText()],
        [sg.Text('Elije dificultad a modificar: '), sg.Button("FACIL", key="-FACIL-",font=('Arial',10)), sg.Button("MEDIA", key="-MEDIA-",font=('Arial',10)), sg.Button("DIFICIL", key="-DIFICIL-",font=('Arial',10))],
        [sg.Button('Parámetros por defecto', key="-DEFAULT-"), sg.Button('Cancelar', key="-CANCELAR-")] 
    ]
    return layout

"""-------------------------LOGÍSTICA------------------------------"""
def logistica(event, values):
    match event:
        case '-FACIL-':
            values_to_options(options_copy, values, 'Facil')
            guardar_parametros(options_copy)
            return False
        case '-MEDIA-':
            values_to_options(options_copy, values, 'Media')
            guardar_parametros(options_copy)
            return False
        case '-DIFICIL-':
            values_to_options(options_copy, values, 'Dificil')
            guardar_parametros(options_copy)
            return False
        case '-DEFAULT-':
            guardar_parametros(options)
            return False
        case '-CANCELAR-':
            return False
    return True


"""-------------------------EJECUCIÓN------------------------------"""
def ejecutar():
    layout=interface()
    crear_ventana("Selección de dificultad", layout,acciones=logistica)
