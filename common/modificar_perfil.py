import os
import json
from common.usuario import Usuario

def editar_perfil(nick:str,edad:str,genero:str):
    """
        Edita los datos del perfil si el nick ingresado existe
    """
    
    usuario = Usuario(nick,edad,genero,'0')
    if (not edad.isnumeric()):
        return False
    ruta=os.path.join(os.getcwd(),'data','json','usuarios_datos')
    try:
        with open(ruta, "r",encoding='utf-8') as arch_usuarios:
            datos_arch = json.load(arch_usuarios)

        exito,datos_arch = modificar(datos_arch,usuario)

        if exito:
            with open(ruta, "w",encoding='utf-8') as arch_usuarios:
                json.dump(datos_arch, arch_usuarios,indent=4)

        return exito
    except FileNotFoundError:
        return False
    

def modificar(datos_arch:list,usuario:Usuario):
    """
        Devuelve True si el nick a ingresar existe y modifica  y devuelve los respectivos datos. 
        Caso contrario devuelve False
    """
    usuario_buscado = list(filter(lambda x: x['nick']==usuario.nick,datos_arch))

    exito = usuario_buscado !=[]

    if exito:
        usuario_buscado[0]['edad'] = usuario.edad
        usuario_buscado[0]['genero'] = usuario.genero

        datos_arch = list(filter(lambda x: x['nick']!=usuario.nick,datos_arch))

        datos_arch.append(usuario_buscado[0])

    return exito,datos_arch