import os
import json

def verificar_perfil(nick:str,contraseña:str):
    """
        Devuelve True si existe el nick y la contraseña es correcta.
        Caso contrario devuelve False
    """

    ruta=os.path.join(os.getcwd(),'data','json','usuarios_datos')
    
    try:
        with open(ruta, "r",encoding='utf-8') as arch_usuarios:
            datos_arch = json.load(arch_usuarios)

            x = filter(
            lambda x: x['nick']==nick and x['contraseña'] == contraseña,datos_arch
            )
            return list(x)!=[]

    except FileNotFoundError:
        return False
