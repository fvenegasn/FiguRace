import json
import os
from typing import Any

def guardar_dato(dato:str,clave:str) -> None:
    """
        función 'guardar_dato'
        
        Def:
            Guarda en el archivo del juego el dato enviado en dato

        Args:
            dato(str): dato a guardar
            clave(str): tipo de dato (perfil,dificultad,dataset)
    """
    ruta=os.path.join(os.getcwd(),'data','json','datos_juego.json')
    with open(ruta,"r+",encoding='utf-8') as archivo:
        
        datos = json.load(archivo)
        datos[clave] = dato
        datos = json.dumps(datos,indent=4) 
        archivo.seek(0)
        archivo.write(datos)
        archivo.truncate()


def mostrar_seleccionado(clave:str) -> Any:
    """
        función 'mostrar_seleccionado'
        
        Def:
            Retorna el dato guardado en ruta con la clave pasada por parametro
        
        Args:
            clave(str): clave del diccionario de los datos del juego (perfil,dificultad,dataset)
        
        retorna el valor de ese clave
    """
    ruta=os.path.join(os.getcwd(),'data','json','datos_juego.json')
    try:
        with open(ruta,"r") as archivo:
            datos = json.load(archivo)
            return datos[clave]
    except FileNotFoundError:
        return f"No hay {clave} seleccionado"