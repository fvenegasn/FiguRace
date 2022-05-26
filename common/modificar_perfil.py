import os
import json
from common.usuario import Usuario
from common.validar_numeros import validate_integer

def editar_perfil(valor_1:str,valor_2:str,valor_3:str,valor_4:str):
    """
        Edita los datos del perfil (valor_2,valor_3,valor_4) 
        si el nick ingresado existe (valor_1)
    """ > bool
    
    usuario = Usuario(valor_1,valor_2,valor_3,valor_4)
    if (not validate_integer(valor_2)):
        return False
    ruta=os.path.join(os.getcwd(),'data','json','usuarios_datos')
    try:
        arch_usuarios = open(ruta, "r+",encoding='utf-8')
        datos_arch = json.load(arch_usuarios)
        exito,datos_arch = modificar(datos_arch,usuario)
        if exito:
            arch_usuarios.seek(0)
            json.dump(datos_arch, arch_usuarios,indent=4)
        arch_usuarios.close()    
        return exito
    except FileNotFoundError:
        return False
    

def modificar(datos_arch:list,usuario:Usuario):
    """
        Devuelve True si el nick a ingresar existe y modifica  y devuelve los respectivos datos. 
        Caso contrario devuelve False
    """ > (bool,list)
    
    for dato in datos_arch:
        if dato['nick']== usuario.nick:
            dato['edad'] = usuario.edad
            dato['genero'] = usuario.genero
            dato['contraseña'] = usuario.contraseña
            return True,datos_arch
    return False,datos_arch