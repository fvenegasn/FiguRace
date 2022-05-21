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
    
    window = sg.Window(name,layout,finalize=True)
    
    loop = True
    while loop:
        event,values = window.read()
        match event:
            case None |sg.WIN_CLOSED:
                break
        window.Hide()
        loop = acciones(event,values)
        window.UnHide()
    window.close()   

# def renderizar_ventana(ventana_actual:sg.Window,ventana_siguiente:sg.Window):
#     """
#     function `renderizar_ventana`
#     Def:
#         Esta funcion se basa en ocultar una ventana actual para ejecutar otra ventana enviada por parametro
#     Args:
#         ventana_actual(sg.Window): Ventana actual del sistema
#         ventana_siguiente (sg.Window): Ventana la cual se quiere renderizar
#     """
#     ventana_actual.Hide()
#     ventana_siguiente.ejecutar()  # type: ignore
#     ventana_actual.UnHide()