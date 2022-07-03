import PySimpleGUI as sg 
from common.hacer_ventana import crear_ventana
from helpers.mejores_puntajes import mejores_promedios, mejores_puntajes

"""-------------------------INTERFAZ------------------------------"""
def interface():
    
    layout = [
        [sg.Text("MEJORES PUNTAJES ",font=('Arial',14))],
        [mejores_puntajes('facil'),mejores_puntajes('media'),mejores_puntajes('dificil')],
        [sg.Text("PUNTAJES PROMEDIOS",font=('Arial',14))],
        [mejores_promedios('facil'),mejores_promedios('media'),mejores_promedios('dificil')],
        [sg.Column([[sg.Button("Volver al menú", key="-VOLVER-",font=('Arial',12))]],justification='right')],
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
