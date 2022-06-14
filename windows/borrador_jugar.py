from common.manejo_datos_juego import mostrar_seleccionado, parametros_configuracion,puntaje_usuario
import PySimpleGUI as sg
from helpers.elegir_opciones import opciones_random

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

caracteristicas,nombre_correcta,nombre_incorrectas = opciones_random(dataset_actual,cant_caracteristicas)

incorrectas = [
        *[[sg.Button(x,key=x,border_width=2,button_color='LavenderBlush3',size=(20,1))]for x in nombre_incorrectas],
    ]

correcta = [sg.Button('Correcta',key='--CORRECTA--',border_width=2,button_color='LavenderBlush3',size=(20,1))]

opciones = [incorrectas,correcta]