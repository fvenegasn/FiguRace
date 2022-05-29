import os
import json
from common.parametros import options


def to_default():
    ruta = os.path.join(os.getcwd(), 'data','json',"configuracion.json")
    with open (ruta, "w", encoding="UTF-8") as archivo:
        json.dump (options, archivo, indent=4)