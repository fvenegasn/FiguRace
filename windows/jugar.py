import PySimpleGUI as sg
from common.generar_tarjeta import generar_tarjeta
from common.hacer_ventana import crear_ventana,pasar_ventana
import os
from common.manejo_datos_juego import guardar_partida, mostrar_seleccionado, parametros_configuracion,puntaje_usuario
import time
from common.partida import Partida
from helpers.generar_id import gen_id
from windows import siguiente_tarjeta

def interfaz():

    #"----------------Variables del juego------------------"
    nick = mostrar_seleccionado('perfil')
    dataset_actual = mostrar_seleccionado('dataset')
    dificultad_actual = mostrar_seleccionado('dificultad')
    parametro = parametros_configuracion(dificultad_actual)
    tiempo_limite = '00:'+str(parametro["tiempo_limite"])
    cant_caracteristicas = parametro["cant_caracteristicas"]

    #"-------------------------------------------------------"
    #mostrar en pantalla nick y dificultad_actual
    perfil = [
            [sg.Text("Figuracer: ",font=('Arial',15)),
            sg.Text(nick,font=('Arial',15),background_color='LavenderBlush3')
            ]
        ]
    dificultad = [
            [sg.Text("Dificultad:",font=('Arial',15)),
            sg.Text(dificultad_actual,font=('Arial',15),background_color='LavenderBlush3')
            ]
        ]
    config =[
            [sg.Column(perfil)],
            [sg.Column(dificultad)],
    ]

    #mostrar en pantalla nick,data_set y dificultad_actual
    ruta_imagen = os.path.join(os.getcwd(),'static',dataset_actual.lower()+'.png') #dependera del dataset elegido
 
    opciones,pistas,respuesta = generar_tarjeta(dataset_actual,cant_caracteristicas)

    layout_tarjeta = [
        [sg.Column(pistas,element_justification='left')],
        [sg.Column(opciones,element_justification='center',background_color='grey',key='-OPCIONES-')],
        ]
    
    columna1 = [
        [sg.Frame(layout=config,title='')],
        [sg.Text('Categoria',font=('Arial',20))],
        [sg.Text(dataset_actual,font=('Arial',15))],
        [sg.Image(filename = ruta_imagen)],
        [sg.Text('Tiempo restante',font=('Arial',20))],
        [sg.Text(tiempo_limite,key='-TEMPORIZADOR-',font=('Arial',20))],
        [sg.Button('Abandonar juego',font=('Arial',10),key='cancelada,fin,-',border_width=2,size=(12,1))]
    ]

    layout=[[sg.Column(columna1),sg.Column(layout_tarjeta,element_justification='center',background_color='grey')]]
    return layout,respuesta

"""-------------------------LOGÍSTICA------------------------------"""
def logistica(event,values,respuesta,**kwargs):
    data=kwargs['data']
    termino_el_juego = data['ronda'] == data['cant_rondas']
    id_partida = data["id_partida"]
    usuarie = mostrar_seleccionado('perfil')
    nivel = mostrar_seleccionado('dificultad')
    genero = data["genero"]

    #--------------ACTUALIZACION--TEMPORIZADOR------------#
    window = kwargs['window']
    tiempo_restante = int(data['tiempo_limite'] - (time.time() - data['tiempo_inicial']))
    tiempo = '0'+str(tiempo_restante) if tiempo_restante<10 else str(tiempo_restante)
    window['-TEMPORIZADOR-'].update('00:'+tiempo)

    if tiempo_restante <= 0:
        sg.Popup('Se acabo el tiempo!')
        partida = Partida(int(time.time()),id_partida,'intento',usuarie,'timeout','-',respuesta,nivel,genero)
        #partida se guarda en pandas --> llamar funcion que lo haga
        guardar_partida(partida)
        pasar_ventana(window,siguiente_tarjeta.ejecutar)
        return False

    #-------------------EVENTOS---------------------#
    #event = key = estado,evento,texto_ingresado,respuesta

    eventos = event.split(',')
    estado = eventos[0]
    if len(eventos) > 2: #casos en el que se clickea alguna opcion o se abandona el juego
        evento = eventos[1].strip('012')
        texto_ingresado = eventos[2]

        partida = Partida(int(time.time()),id_partida,evento,usuarie,estado,texto_ingresado,respuesta,nivel,genero)
        #partida se guarda en pandas --> llamar funcion que lo haga
        guardar_partida(partida)

    match estado:
        case "ok":
            sg.Popup('Muy bien!')
            data['puntaje'] = data['puntaje'] + data["rta_correcta"]
        case "error":
            sg.Popup(f"Incorrecto :( La respuesta correcta es {respuesta}")
            data['puntaje'] = data['puntaje'] - data["rta_incorrecta"]

    match estado:
        case "ok" | "error":
            if not termino_el_juego:
                pasar_ventana(window,siguiente_tarjeta.ejecutar)
            else:
                partida = Partida(int(time.time()),id_partida,'fin',usuarie,'finalizada','-','-',nivel,genero)
                # partida se guarda en panda --> llamar funcion que lo haga
                guardar_partida(partida)
                
                sg.Popup(f"Terminaste la partida con un puntaje de {data['puntaje']}")
                # if data['puntaje'] > data['puntaje_max'] guardar en el json
            return False
        case 'cancelada':
            sg.Popup('Abandona')
            return False
    return True

"""-------------------------INICIALZACIÓN SESIÓN------------------------------"""
def initialize(data):
    data["ronda"] = 1
    data["tiempo_inicial"] = time.time()
    data["id_partida"] = gen_id()
    usuarie = mostrar_seleccionado('perfil')
    nivel = mostrar_seleccionado('dificultad')
    data["genero"] = mostrar_seleccionado('dataset')
    data["puntaje_max"] = puntaje_usuario(usuarie,nivel)
    data["puntaje"] = 0
    parametro = parametros_configuracion(nivel)
    data["tiempo_limite"] = parametro["tiempo_limite"]
    data["cant_rondas"] = parametro["cant_rondas"]
    data["rta_correcta"] = parametro["rta_correcta"]
    data["rta_incorrecta"] = parametro["rta_incorrecta"]
    
    partida_inicio = Partida(int(data["tiempo_inicial"]),data["id_partida"],'inicio_partida',usuarie,'-','-','-',nivel,data["genero"])
    guardar_partida(partida_inicio)

"""-------------------------EJECUCIÓN------------------------------"""
def ejecutar():
    layout,respuesta = interfaz()
    crear_ventana("Pantalla de Juego", layout,logistica,initialize=initialize,respuesta= respuesta)
    