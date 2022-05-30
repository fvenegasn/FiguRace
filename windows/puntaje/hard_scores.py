import PySimpleGUI as sg
from common.hacer_ventana import crear_ventana

"""-------------------------INTERFAZ------------------------------"""
def interface():
    name_column = [
        [sg.Text("Nick",font=('Arial',10))],
        [sg.Text("Fran",font=('Arial',10))],
        [sg.Text("Oli",font=('Arial',10))],
        [sg.Text("Ati",font=('Arial',10))],
        [sg.Text("Fefe",font=('Arial',10))],
        [sg.Text("Gua",font=('Arial',10))],
        [sg.Text("Facu",font=('Arial',10))],
        [sg.Text("El negro",font=('Arial',10))],
        [sg.Text("Tebi",font=('Arial',10))],
        [sg.Text("Joacko",font=('Arial',10))],
        [sg.Text("Joao",font=('Arial',10))],
        [sg.Text("Fabo",font=('Arial',10))],
        [sg.Text("Alvarez",font=('Arial',10))],
        [sg.Text("Julian",font=('Arial',10))],
        [sg.Text("Luqi",font=('Arial',10))],
        [sg.Text("Dante",font=('Arial',10))],
        [sg.Text("Seba",font=('Arial',10))],
        [sg.Text("Juli",font=('Arial',10))],
        [sg.Text("Emi",font=('Arial',10))],
        [sg.Text("Cris",font=('Arial',10))],
        [sg.Text("Juan",font=('Arial',10))],
    ]
    score_column = [
        [sg.Text("Score",font=('Arial',10))],
        [sg.Text("20",font=('Arial',10))],
        [sg.Text("19",font=('Arial',10))],
        [sg.Text("18",font=('Arial',10))],
        [sg.Text("17",font=('Arial',10))],
        [sg.Text("16",font=('Arial',10))],
        [sg.Text("10",font=('Arial',10))],
        [sg.Text("14",font=('Arial',10))],
        [sg.Text("13",font=('Arial',10))],
        [sg.Text("12",font=('Arial',10))],
        [sg.Text("11",font=('Arial',10))],
        [sg.Text("10",font=('Arial',10))],
        [sg.Text("9",font=('Arial',10))],
        [sg.Text("8",font=('Arial',10))],
        [sg.Text("7",font=('Arial',10))],
        [sg.Text("6",font=('Arial',10))],
        [sg.Text("5",font=('Arial',10))],
        [sg.Text("4",font=('Arial',10))],
        [sg.Text("3",font=('Arial',10))],
        [sg.Text("2",font=('Arial',10))],
        [sg.Text("1",font=('Arial',10))],
    ]

    layout = [
        [sg.Text("MEJORES PUNTAJES (Dificil)",font=('Arial',17))],
        [sg.Column(name_column),sg.Column(score_column, element_justification='c')],
        [sg.Button("Volver", key="-VOLVER-",font=('Arial',14))],
    ]
    return layout

"""-------------------------LOGÍSTICA------------------------------"""
def logistica(event,values):
    match event:
        case '-VOLVER-':
            return False
    return True

"""-------------------------EJECUCIÓN------------------------------"""
def ejecutar():
    layout = interface()
    crear_ventana('Mejores puntuaciones (Dificil)',layout,acciones=logistica)