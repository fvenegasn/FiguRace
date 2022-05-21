import PySimpleGUI as sg

def crear_ventana(name,layout,acciones):
    """
    funcion crear_ventana
    
    Def:
        Esta funcion crea una ventana con los atributos pasados y crea un loop que permite la interacción con la misma

    Args:
        name(str): nombre de la ventana a crear
        layout(list): contenido de la ventana a crear
        acciones(funcion): funcion que contiene la logistica de la ventana a crear
    """
    window = sg.Window(name,layout)
    loop = True
    while True and loop:
        event,values = window.read()
        match event:
            case[None,'-VOLVER-',sg.WIN_CLOSED]:
                window.close()
                break
        loop = acciones(event,values)

#def renderiz():
#    t=0