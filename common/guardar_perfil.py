import os
import json
from common.Usuario import Usuario

def guardar_perfil(valor_1,valor_2,valor_3):
    """Retorna True si se pudo guardar con exito el nuevo usuario"""

    usuario = Usuario(valor_1,valor_2,valor_3)
    dato_ingresar = usuario.generar_dicci()
    return guardar_en_archivo(dato_ingresar)

def guardar_en_archivo(dato_in):
    """Guarda nuevo usuario en archivo si el nick no es uno ya existente y
    devuelve True. Caso contrario devuelve False"""
    
    ruta=os.path.join(os.getcwd(),'data','json','usuarios_datos')
    exito = True
    try:
        arch_usuarios = open(ruta, "r+")
        datos_arch = json.load(arch_usuarios)
        #Me fijo si el nick ya existe
        nick = dato_in['nick']
        if existe(datos_arch,nick):
            exito = False
        else:
            datos_arch.append(dato_in)
            arch_usuarios.seek(0)
            json.dump(datos_arch, arch_usuarios,indent=4)
    except FileNotFoundError:
        arch_usuarios = open(ruta,'x')
        json.dump([dato_in],arch_usuarios,indent=4)
        arch_usuarios.close()
    return exito

def existe(datos_arch,nick):
    """Devuelve True si el nick a ingresar ya existe. Caso contrario devuelve False"""
    for usuario in datos_arch:
        if usuario['nick']==nick:
            return True
    return False

