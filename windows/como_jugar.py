import PySimpleGUI as sg
from common.hacer_ventana import crear_ventana
import os

def abrir_explicacion_juego():
    archivo_path=os.path.join(os.getcwd(),'static','explicacion_juego')
    try:
        with open(archivo_path,'r',encoding='utf-8') as archivo:
            return archivo.read()
    except FileNotFoundError:
        print(f'No se encontro el archivo{archivo_path}')
        exit(1) 
    

"""-------------------------INTERFAZ-------------------------------"""
def interface():
    explicacion=abrir_explicacion_juego()
    layout=[
        [sg.Text('Cómo Jugar', font=(any,20),justification='center')],
        [sg.Text(explicacion,font=('Arial',15),justification='center')],
        [sg.Button('Volver',key='-VOLVER-',)],
    ]
    return layout

"""-------------------------LOGÍSTICA------------------------------"""
def logistica(event,values):
    match event:
        case '-VOLVER-':
            return False
    return True


"""-------------------------EJECUCIÓN------------------------------"""
def ejecutar():
    layout=interface()
    crear_ventana("Pantalla de Juego", layout,acciones=logistica)