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
        datos_juego_default()

def datos_juego_default():
    """
        Guarda en archivo la configuracion por default de los datos del juego
    """
    
    datos_default = {
            "perfil": "-None-",
            "dificultad": "Media",
            "dataset": "Spotify"
            }
    escribir_json_data(datos_default,ruta_datos_juego)

def parametros_configuracion(dificultad:str):
    
    """
        Retorna diccionario de la configuración de la dificultad pasada como parámetro
    """

    datos = leer_json_data(ruta_configuracion)
    return datos[dificultad] if datos else False
    
def buscar_usuario(nick:str)-> dict: 
    """
    funcion 'buscar_usuario'
    
    Def:
        Retorna los datos del usuario pasado como parámetro
    """
    datos = leer_json_data(ruta_usuarios_datos)
    return list(filter(lambda x: x['nick'] == nick,datos))[0]

def guardar_en_csv(ruta:str,fila:pd.Series,columnas:list):
    """
    funcion 'guardar_en_csv'

    Def:
        Guarda en un archivo csv la información pasada como parametro
    
    Args:
        ruta(str): es la ruta del archivo a agregar fila
        fila(pd.Series): es la nueva información a agregar
        columnas(list[str]): son las columnas que componen a csv, en caso de que el csv no se haya creado
    """
    try:
        df=pd.read_csv(ruta) 
    except:
        df = pd.DataFrame(columns=columnas)
    
    df=df.append(fila,ignore_index=True)
    df.to_csv(ruta,index=False)

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
    columnas= ['Timestamp', 'Id', 'Evento', 'Usuarie', 'Estado', 'Texto Ingresado', 'Respuesta', 'Nivel','Genero', 'Dataset']
    guardar_en_csv(ruta,fila,columnas)

def guardar_puntaje(nick:str,puntaje:int,nivel:str):
    """
    funcion 'guardar_puntaje'

    Def:
        Guarda en un archivo csv de los puntajes de cada nivel, el usuario y un nuevo puntaje
    
    Args:
        nick(str): usuario correspondiente
        puntaje(int): puntaje de la partida 
        nivel(str): es el nivel en el que usuario obtuvo el puntaje
    """

    data={
        'Nick' : nick, 
        'Puntaje' : puntaje  
    }
    ruta = os.path.join(ruta_csv,'puntajes_'+nivel.lower()+'.csv')
    fila = pd.Series(data)
    columnas=['Nick','Puntaje']
    guardar_en_csv(ruta,fila,columnas)

def guardar_puntaje_maximo(nick:str,puntaje:int,dificultad:str):
    """
    funcion 'guardar_puntaje_maximo'

    Def:
        guarda el nuevo puntaje maximo, en el nivel correspondiente, del usuario en un archivo json
        que contiene los datos de los usuarios
    
    Args:
        nick(str): nick del usuario que jugó
        dificultad(str): nivel jugado
        puntaje(int): nuevo puntaje maximo
    """
    datos=leer_json_data(ruta_usuarios_datos)
    dato=list(filter(lambda x: x['nick'] == nick,datos))[0]
    index=datos.index(dato)

    dato['puntaje'][dificultad] = puntaje
    datos[index]=dato
    escribir_json_data(datos,ruta_usuarios_datos)
    