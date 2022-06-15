import PySimpleGUI as sg
from common.generar_tarjeta import generar_tarjeta
from common.hacer_ventana import crear_ventana
import os
from common.manejo_datos_juego import mostrar_seleccionado, parametros_configuracion,puntaje_usuario
import time
from common.partida import Partida

def interfaz(tiempo_inicial):

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

    id_partida ="33ff0802-e53f-11ec-8fea-0242ac120002" # debo generar id aleatorio
    datos_partida_inicio = Partida(id_partida,'inicio_partida',nick,' ','-','-',dificultad_actual)
    #estos datos de la partida se deben guardar en archivo csv

    #"-------------------------------------------------------"

    ruta_imagen = os.path.join(os.getcwd(),'static','lagos.png') #dependera del dataset elegido
 
    opciones,pistas,nombre_correcta = generar_tarjeta(dataset_actual,cant_caracteristicas)

    layout_tarjeta = [
        [sg.Column(pistas,element_justification='left',key='-PISTAS-')],
        [sg.Column(opciones,element_justification='center',background_color='grey',key='-OPCIONES-')],
        [sg.Button('PASAR',key='-PASAR-')]
        ]
    
    columna1 = [
        [sg.Text('Categoria',font=('Arial',20))],
        [sg.Text(dataset_actual,font=('Arial',15))],
        [sg.Image(filename = ruta_imagen)],
        [sg.Text('Tiempo restante',font=('Arial',20))],
        [sg.Text(int(tiempo_limite - (time.time() - tiempo_inicial)),key='-TEMPORIZADOR-',font=('Arial',20))],
        [sg.Button('Abandonar juego',font=('Arial',10),key='finalizada,-,fin',border_width=2,size=(12,1))]
    ]

    layout=[[sg.Column(columna1),sg.Column(layout_tarjeta,element_justification='center',background_color='grey')]]
    return layout

"""-------------------------LOGÍSTICA------------------------------"""
def logistica(event,values):

    eventos = event.split(',')
    estado = eventos[0]
    texto_ingresado = eventos[1] if len(eventos) > 1 else " "
    evento = eventos[2] if len(eventos) > 2 else " "
    dato_evento = Partida('id_partida',evento,'nick',estado,texto_ingresado,'nombre_correcta','nivel')

    # ver como pasar los parametros id,nick,nombre_correcta y nivel que estan en funcion interfaz

    match estado:
        case "ok":
            sg.Popup('Es la correcta')
            #actualizar la tarjeta
        case "error" | "error0" | "error1" | "error2":
            sg.Popup('Esa no es')
            #actualizar la tarjeta
        case '-PASAR-':
            #actualizar la tarjeta
            sg.Popup('Pasa a la siguiente')
        case 'finalizada':
            return False
    return True

def update_windows(window):
    window['-TEMPORIZADOR-'].update(int(time.time())) 
    #preguntar como pasar parametro del tiempo inicial
    #window['-TEMPORIZADOR-'].update(int(time.time() - tiempo_inicial)) 

"""-------------------------EJECUCIÓN------------------------------"""
def ejecutar():
    tiempo_inicial = time.time()

    layout = interfaz(tiempo_inicial)
    crear_ventana("Pantalla de Juego", layout,logistica,update_windows=update_windows)
    