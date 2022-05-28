from encodings import utf_8
import os
import json
from common.guardar_perfil import existe


def verificar_perfil(nick:str,contraseña:str):
    """
        Devuelve True si existe el nick y la contraseña es correcta.
        Caso contrario devuelve False
    """

    ruta=os.path.join(os.getcwd(),'data','json','usuarios_datos')
    
    try:
        with open(ruta, "r",encoding='utf-8') as arch_usuarios:
            datos_arch = json.load(arch_usuarios)

            for usuario in datos_arch:
                if usuario['nick']==nick:
                    return usuario['contraseña']==contraseña
            return False
    except FileNotFoundError:
        return False
