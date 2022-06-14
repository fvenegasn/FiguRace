import os
import json

ruta_json = os.path.join(os.getcwd(),'data','json')

ruta_usuarios_datos = os.path.join(ruta_json,'usuarios_datos')

ruta_configuracion = os.path.join(ruta_json,'configuracion.json')

ruta_datos_juego = os.path.join(ruta_json,'datos_juego.json')

ruta_csv = os.path.join(os.getcwd(),'data','csv')

def obtener_datos(ruta:str):
    
    """
        Devuelve los datos de un archivo ubicado en ruta si existe, sino devuelve false
    """
    
    try:
        with open(ruta,"r",encoding='utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return False