import os
import json
from common.parametros import options


def guardar_parametros(datos:dict) -> None:
    """
    funcion 'to_default'

    Def:
        Escribe el archivo que contiene los parámetros de la configuración del juego a su configuración por defecto
    """
    ruta = os.path.join(os.getcwd(), 'data','json',"configuracion.json")
    with open (ruta, "w", encoding="UTF-8") as archivo:
        json.dump (datos, archivo, indent=4)