from textwrap import indent
import PySimpleGUI as sg
from common.hacer_ventana import crear_ventana
from helpers.elegir_opciones import opciones_random
import os

def interfaz():
    ruta_imagen = os.path.join(os.getcwd(),'static','lagos.png')
 
    categorias = [
        [sg.Text("Ubicación: ",font=('Arial',12)),sg.Text("Santa Cruz",font=('Arial',12),justification="right")],
        [sg.Text("Superficie (km²): ",font=('Arial',12)),sg.Text("1435 ",font=('Arial',12))],
        [sg.Text("Profundidad máxima (m): ",font=('Arial',12)),sg.Text("500",font=('Arial',12))],
        [sg.Text("Profundidad media (m): ",font=('Arial',12)),sg.Text("150",font=('Arial',12))],
        [sg.Text("Coordenadas: ",font=('Arial',12)),sg.Text("-50.248 / -72.645",font=('Arial',12))],
        [sg.Text("Nombre: ",font=('Arial',12))]
    ]


    lista_opciones = opciones_random('Lagos',correcta='Lago Cardiel')
    
    opciones = [
        *[[sg.Button(x,key=x,border_width=2,button_color='LavenderBlush3',size=(20,1))]for x in lista_opciones],
    ]
    
    
    layout_tarjeta = [
        [sg.Column(categorias,element_justification='left')],
        [sg.Column(opciones,element_justification='center',background_color='grey')],
        [sg.Button('OK'),sg.Button('PASAR')]
        ]
    
    columna1 = [
        [sg.Text('Categoria',font=('Arial',20))],
        [sg.Text('Lagos',font=('Arial',15))],
        [sg.Image(filename = ruta_imagen)],
        [sg.Text('Temporizador',font=('Arial',20))],
        [sg.Text('00:30',font=('Arial',20))],
        [sg.Button('Volver al menú',font=('Arial',15),key='-VOLVER-',border_width=2,size=(12,1))]
    ]

    layout=[[sg.Column(columna1),sg.Column(layout_tarjeta,element_justification='center',background_color='grey')]]
    return layout

"""-------------------------LOGÍSTICA------------------------------"""
def logistica(event,values):
    match event:
        case '-VOLVER-':
            return False
    return True

"""-------------------------EJECUCIÓN------------------------------"""
def ejecutar():
    layout = interfaz()
    crear_ventana("Pantalla de Juego", layout,logistica)
