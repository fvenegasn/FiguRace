import PySimpleGUI as sg
from common.hacer_columnas_puntajes import make_columns
from common.hacer_ventana import crear_ventana


"""-------------------------INTERFAZ------------------------------"""
def interface():
    archivo = 'puntajes_media.csv'
    columna_nombres, columna_puntajes = make_columns(archivo)
    
    layout = [
        [sg.Text("MEJORES PUNTAJES (Media)",font=('Arial',16))],
        [sg.Column(columna_nombres),sg.Column(columna_puntajes, element_justification='c')],
        [sg.Button("Volver", key="-VOLVER-",font=('Arial',14))],
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
    layout = interface()
    crear_ventana('Mejores puntuaciones (Media)',layout,acciones=logistica)