import os
import json
from common.usuario import Usuario

def guardar_perfil(nick:str, edad:str, genero:str, contraseña:str):
    """Retorna True si se pudo guardar con exito el nuevo usuario"""
    
    if (not edad.isnumeric()):
        return False
    else:
        usuario = Usuario(nick,edad,genero,contraseña)
        dato_ingresar = usuario.generar_dicci()
        return guardar_en_archivo(dato_ingresar)


def guardar_en_archivo(dato_in:dict):
    """
        Guarda nuevo usuario en archivo si el nick no es uno ya existente y devuelve True. 
        Caso contrario devuelve False
    """
    
    ruta=os.path.join(os.getcwd(),'data','json','usuarios_datos')
    exito = False
    try:
        arch_usuarios = open(ruta, "r+",encoding='utf-8')
        datos_arch = json.load(arch_usuarios)
        #Me fijo si el nick ya existe
        nick = dato_in['nick']
        if not existe(datos_arch,nick):
            exito = True
            datos_arch.append(dato_in)
            arch_usuarios.seek(0)
            json.dump(datos_arch, arch_usuarios,indent=4)
    except FileNotFoundError:
        exito = True
        arch_usuarios = open(ruta,'x')
        json.dump([dato_in],arch_usuarios,indent=4)
    arch_usuarios.close()
    return exito

def existe(datos_arch:list,nick:str):
   
    """
        Devuelve True si el nick a ingresar ya existe. 
        Caso contrario devuelve False
    """
    
    x = filter(lambda x: x['nick']==nick,datos_arch)

    return list(x)!=[]

