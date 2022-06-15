from helpers.elegir_opciones import opciones_random
import random
import PySimpleGUI as sg


def generar_tarjeta(dataset_actual,cant_caracteristicas):
    
    caracteristicas,nombre_correcta,nombre_incorrectas = opciones_random(dataset_actual,cant_caracteristicas)

    #----BOTONES DE OPCIONES DISPUESTOS EN FORMA ALEATORIA----#
    correcta = [sg.Button(nombre_correcta,key="ok,"+nombre_correcta + ",intento",border_width=2,button_color='LavenderBlush3',size=(20,1))]

    opciones = [[sg.Button(x,key="error," + x + ",intento",border_width=2,button_color='LavenderBlush3',size=(20,1))] for x in nombre_incorrectas]

    opciones.insert(random.randrange(5),correcta)

    pistas = [[sg.Text(x,font = ('Arial,12'))] for x in caracteristicas]

    return opciones,pistas,nombre_correcta