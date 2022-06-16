import PySimpleGUI as sg
from common.generar_tarjeta import generar_tarjeta
from common.hacer_ventana import crear_ventana,pasar_ventana
import os
from common.manejo_datos_juego import mostrar_seleccionado, parametros_configuracion,puntaje_usuario
import time
from common.partida import Partida
from windows import siguiente_tarjeta

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
        [sg.Column(pistas,element_justification='left',key='holis')],
        [sg.Column(opciones,element_justification='center',background_color='grey',key='-OPCIONES-')],
        ]
    
    columna1 = [
        [sg.Text('Categoria',font=('Arial',20))],
        [sg.Text(dataset_actual,font=('Arial',15))],
        [sg.Image(filename = ruta_imagen)],
        [sg.Text('Tiempo restante',font=('Arial',20))],
        [sg.Text(tiempo_limite,key='-TEMPORIZADOR-',font=('Arial',20))],
        [sg.Button('Abandonar juego',font=('Arial',10),key='cancelada,fin,-,-',border_width=2,size=(12,1))]
    ]

    layout=[[sg.Column(columna1),sg.Column(layout_tarjeta,element_justification='center',background_color='grey')]]
    return layout

"""-------------------------LOGÍSTICA------------------------------"""
def logistica(event,values,**kwargs):
    #--------------ACTUALIZACION--TEMPORIZADOR------------#
    window = kwargs['window']
    data=kwargs['data']
    window['-TEMPORIZADOR-'].update(int(data['tiempo_limite'] - (time.time() - data['tiempo_inicial'])))
    #-------------------EVENTOS---------------------#
    #event = key = estado,evento,texto_ingresado,respuesta
    eventos = event.split(',')
    estado = eventos[0]
    if len(eventos) > 3:
        evento = eventos[1].strip('012')
        texto_ingresado = eventos[2]
        respuesta = eventos[3]
        id_partida = data["id_partida"]
        usuarie = mostrar_seleccionado('perfil')
        nivel = mostrar_seleccionado('dificultad')
        dato_evento = Partida(int(time.time()),id_partida,evento,usuarie,estado,texto_ingresado,respuesta,nivel)
        #dato_evento se guarda en pandas

    match estado:
        case "ok":
            sg.Popup('Es la correcta')
            #actualizar la tarjeta, tiempo por ronda y puntaje
            pasar_ventana(window,siguiente_tarjeta.ejecutar)
            return False
        case "error":
            sg.Popup('Esa no es')
            #actualizar la tarjeta, tiempo por ronda y puntaje
            pasar_ventana(window,siguiente_tarjeta.ejecutar)
            return False

        #case 'finalizada':
            #finalizaron todas las rondas, se actualiza puntaje
        case 'cancelada':
            #no registrar puntaje si la partida se abandono
            return False
    return True


def initialize(data):
    data["tiempo_inicial"] = time.time()
    nivel = mostrar_seleccionado('dificultad')
    parametro = parametros_configuracion(nivel)
    data["tiempo_limite"] = parametro["tiempo_limite"]

"""-------------------------EJECUCIÓN------------------------------"""
def ejecutar():
    layout = interfaz()
    crear_ventana("Pantalla de Juego", layout,logistica,initialize=initialize)