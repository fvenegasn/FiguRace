import os
from typing import Any
from common.partida import Partida
from common.paths import ruta_usuarios_datos, ruta_configuracion, ruta_datos_juego,ruta_csv
from common.archivo import leer_json_data,escribir_json_data
import pandas as pd

def guardar_dato(dato:str,clave:str) -> None:
    """
        función 'guardar_dato'
        
        Def:
            Guarda en el archivo del juego el dato enviado en dato

        Args:
            dato(str): dato a guardar
            clave(str): tipo de dato (perfil,dificultad,dataset)
    """
    datos=leer_json_data(ruta_datos_juego)
    datos[clave] = dato
    escribir_json_data(datos,ruta_datos_juego)

def mostrar_seleccionado(clave:str) -> Any:
    """
        función 'mostrar_seleccionado'
        
        Def:
            Retorna el dato guardado en ruta con la clave pasada por parametro
        
        Args:
            clave(str): clave del diccionario de los datos del juego (perfil,dificultad,dataset)
        
        retorna el valor de ese clave
    """
    try:
        datos = leer_json_data(ruta_datos_juego)
        return datos[clave]

    except FileNotFoundError:
        return f"No hay {clave} seleccionado"

def parametros_configuracion(dificultad:str):
    
    """
        Retorna diccionario de la configuración de la dificultad pasada como parámetro
    """

    datos = leer_json_data(ruta_configuracion)
    return datos[dificultad] if datos else False
    
def puntaje_usuario(nick:str,dificultad:str):

    """Retorna puntaje del usuario según la dificultad pasada como parámetro"""

    datos = leer_json_data(ruta_usuarios_datos)

    if datos:
        usuario = list(filter(lambda x: x['nick'] == nick,datos))[0]
        return usuario['puntaje'][dificultad]

def guardar_partida(partida:Partida):
    """
    funcion 'guardar_partida'

    Def:
        Guarda en un archivo csv la información de la partida pasada como parametro
    
    Args:
        partida(Partida): instancia de un objeto Partido. Este objeto cuenta con un método
        'devolver_valores' que retorna un diccionario con sus atributos
    """
    ruta=os.path.join(ruta_csv,'informacion_partidas.csv')

    fila= pd.Series(partida.devolver_valores())
    try:
        partidas=pd.read_csv(ruta) 
    except:
        partidas = pd.DataFrame(columns=['Timestamp', 'Id', 'Evento', 'Usuarie', 'Estado', 'Texto Ingresado', 'Respuesta', 'Nivel','Genero'])
    
    partidas=partidas.append(fila,ignore_index=True)
    partidas.sort_values(by='Id')
    partidas.to_csv(ruta,index=False)