import PySimpleGUI as sg
from common.generar_tarjeta import generar_tarjeta
from common.hacer_ventana import crear_ventana
import os
from common.manejo_datos_juego import mostrar_seleccionado, parametros_configuracion,puntaje_usuario


def interfaz():

    #"----------------Variables del juego------------------"
    nick = mostrar_seleccionado('perfil')
    dataset_actual = mostrar_seleccionado('dataset')
    dificultad_actual = mostrar_seleccionado('dificultad')
    puntaje = puntaje_usuario(nick,dificultad_actual)

    parametro = parametros_configuracion(dificultad_actual)
    tiempo_limite = parametro["tiempo_limite"]
    cant_rondas = parametro["cant_rondas"]
    rta_correcta = parametro["rta_correcta"]
    rta_incorrecta = parametro["rta_incorrecta"]
    cant_caracteristicas = parametro["cant_caracteristicas"]
    #"-------------------------------------------------------"

    ruta_imagen = os.path.join(os.getcwd(),'static','lagos.png') #dependera del dataset elegido
 
    opciones,pistas = generar_tarjeta(dataset_actual,cant_caracteristicas)

    layout_tarjeta = [
        [sg.Column(pistas,element_justification='left')],
        [sg.Column(opciones,element_justification='center',background_color='grey')],
        [sg.Button('PASAR')]
        ]
    
    columna1 = [
        [sg.Text('Categoria',font=('Arial',20))],
        [sg.Text(dataset_actual,font=('Arial',15))],
        [sg.Image(filename = ruta_imagen)],
        [sg.Text('Temporizador',font=('Arial',20))],
        [sg.Text('00:30',font=('Arial',20))],
        [sg.Button('Abandonar juego',font=('Arial',10),key='-VOLVER-',border_width=2,size=(12,1))]
    ]

    layout=[[sg.Column(columna1),sg.Column(layout_tarjeta,element_justification='center',background_color='grey')]]
    return layout

"""-------------------------LOGÍSTICA------------------------------"""
def logistica(event,values):
    match event:
        case "ok":
            sg.Popup('Es la correcta')
            #actualizar la tarjeta
        case "error" | "error0" | "error1" | "error2":
            sg.Popup('Esa no es')
            #actualizar la tarjeta
        case '-VOLVER-':
            return False
    return True

"""-------------------------EJECUCIÓN------------------------------"""
def ejecutar():
    layout = interfaz()
    crear_ventana("Pantalla de Juego", layout,logistica)
