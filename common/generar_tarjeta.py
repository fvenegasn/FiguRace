from helpers.elegir_opciones import opciones_random
import random
import PySimpleGUI as sg


def generar_tarjeta(dataset_actual,cant_caracteristicas):
    
    columnas,caracteristicas,nombre_correcta,nombre_incorrectas = opciones_random(dataset_actual,cant_caracteristicas)

    #----BOTONES DE OPCIONES DISPUESTOS EN FORMA ALEATORIA----#

    correcta = [sg.Button(nombre_correcta,key='ok,intento,'+nombre_correcta+','+nombre_correcta,border_width=2,button_color='LavenderBlush3',size=(40,2),font=('Arial',13))]

    opciones = [[sg.Button(x,key='error,intento,'+x+','+nombre_correcta,border_width=2,button_color='LavenderBlush3',size=(40,2),font=('Arial',13))] for x in nombre_incorrectas]

    opciones.insert(random.randrange(5),correcta)

    pistas=[]
    for i,pista in enumerate(caracteristicas):
        pistas.append([sg.Text(columnas[i]+':',font=('Arial',14)),sg.Text(pista,font=('Arial',12))])

    return opciones,pistas,nombre_correcta