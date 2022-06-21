import PySimpleGUI as sg 
from common.hacer_ventana import crear_ventana
from helpers.mejores_puntajes import hacer_tabla

"""-------------------------INTERFAZ------------------------------"""
def interface():
    
    layout = [
        [sg.Text("MEJORES PUNTAJES ",font=('Arial',16))],
        [hacer_tabla('Nivel Fácil','facil'),hacer_tabla('Nivel Medio','media'),hacer_tabla('Nivel Dificil','dificil')],
        [sg.Column([[sg.Button("Volver al menú", key="-VOLVER-",font=('Arial',14))]],justification='right')],
    ]
    return layout

"""-------------------------LOGÍSTICA------------------------------"""
def logistica(event,values,**kwargs):
    if event=='-VOLVER-':
        return False
    return True

"""-------------------------EJECUCIÓN------------------------------"""
def ejecutar():
    layout = interface()
    crear_ventana('Mejores Puntajes ',layout,acciones=logistica)
