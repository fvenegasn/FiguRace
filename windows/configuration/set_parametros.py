import PySimpleGUI as sg
from common.hacer_ventana import crear_ventana
from windows.configuration import dificultad
from common.to_default import to_default

"""-------------------------INTERFAZ-------------------------------"""
def interface():
    layout = [
        [sg.Text('Ingrese el tiempo límite (en segundos)'), sg.InputText()],
        [sg.Text('Ingrese la cantidad de rondas por juego'), sg.InputText()],
        [sg.Text('Ingrese el puntaje sumado por cada respuesta correcta'), sg.InputText()],
        [sg.Text('Ingrese el puntaje sumado por cada respuesta incorrecta'), sg.InputText()],
        [sg.Text('Ingrese la cantidad de características a mostrar'), sg.InputText()],
        [sg.Button('Elige dificultad a modificar', key="-CONTINUAR-"),sg.Button('Parámetros por defecto', key="-DEFAULT-"), sg.Button('Cancelar', key="-CANCELAR-")] 
    ]
    return layout

"""-------------------------LOGÍSTICA------------------------------"""
def logistica(event, values):
    global dict_values
    global dificultad_modif
    dificultad_modif = "Media" #por defecto
    match event:
        case '-CONTINUAR-':
            dict_values = values
            dificultad_modif = dificultad.ejecutar()
            return False
        case '-DEFAULT-':
            to_default()
            dict_values = None
            return False
        case '-CANCELAR-':
            dict_values = None
            return False
    return True


"""-------------------------EJECUCIÓN------------------------------"""
def ejecutar():
    layout=interface()
    crear_ventana("Selección de dificultad", layout,acciones=logistica)
    return dict_values,dificultad_modif