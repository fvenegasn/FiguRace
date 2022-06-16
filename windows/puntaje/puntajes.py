import PySimpleGUI as sg 
from common.hacer_ventana import crear_ventana,pasar_ventana
from windows.puntaje import easy_scores, hard_scores, medium_scores

"""-------------------------INTERFAZ------------------------------"""
def interface():
    layout = [
        [sg.Text("Seleccione una dificultad",font=('Arial',15))],
        [sg.Button("FACIL", key="-FACIL-",font=('Arial',15))],
        [sg.Button("MEDIA", key="-MEDIA-",font=('Arial',15))],
        [sg.Button("DIFICIL", key="-DIFICIL-",font=('Arial',15))],
        [sg.Button("Volver al menú", key="-VOLVER-",font=('Arial',14))],
    ]
    return layout

"""-------------------------LOGÍSTICA------------------------------"""
def logistica(event,values,**kwargs):
    window = kwargs['window']
    match event:
        case '-FACIL-':
            pasar_ventana(window,easy_scores.ejecutar)
        case '-MEDIA-':
            pasar_ventana(window,medium_scores.ejecutar)
        case '-DIFICIL-':
            pasar_ventana(window,hard_scores.ejecutar)
        case '-VOLVER-':
            return False
    return True

"""-------------------------EJECUCIÓN------------------------------"""
def ejecutar():
    layout = interface()
    crear_ventana('Puntajes',layout,acciones=logistica)
