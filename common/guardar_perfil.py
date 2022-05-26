import os
import json
from common.usuario import Usuario
from common.validar_numeros import validate_integer

def guardar_perfil(valor_1:str,valor_2:str,valor_3:str,valor_4:str):
    """Retorna True si se pudo guardar con exito el nuevo usuario"""
    
    if (not validate_integer(valor_2)):
        return False
    else:
        usuario = Usuario(valor_1,valor_2,valor_3,valor_4)
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
    
    for usuario in datos_arch:
        if usuario['nick']==nick:
            return True
    return False

