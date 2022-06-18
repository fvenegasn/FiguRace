from common.paths import ruta_configuracion
from common.archivo import escribir_json_data

def guardar_parametros(datos:dict) -> None:
    """
    funcion 'guardar_parametros'

    Def:
        Escribe el archivo que contiene los parámetros de la configuración 
        del juego a su configuración por defecto
    """
    escribir_json_data(datos,ruta_configuracion)