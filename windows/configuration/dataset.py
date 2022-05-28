import PySimpleGUI as sg
from common.hacer_ventana import crear_ventana
import helpers.dict_to_str

"""-------------------------INTERFAZ-------------------------------"""
def interface():
    dataset_lista = ['Spotify','Lagos Argentina','Películas']
    dataset=[]
    for elem in dataset_lista:
        dataset.append(
            [sg.Radio(elem,'perfiles',size=(30,30),key=elem)]
        )
    
    layout = [
        [sg.Frame('DATASETS: ',layout=dataset,border_width=30,background_color='green')],
        [sg.Button('ACEPTAR',key='-ACEPTAR-')],
        [sg.Button("Volver al menú", key="-VOLVER-",font=('Arial',13))],
    ]
    return layout

"""-------------------------LOGÍSTICA------------------------------"""
def logistica(event, values):
    global chosen_dataset
    match event:
        case '-ACEPTAR-':
            chosen_dataset = helpers.dict_to_str.procesar_eleccion (values)
            return False
        case '-VOLVER-':
            return False
    return True

"""-------------------------EJECUCIÓN------------------------------"""
def ejecutar():
    layout=interface()
    crear_ventana("Selección de Dataset", layout,acciones=logistica)
    return chosen_dataset