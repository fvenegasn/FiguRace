import os
import json
from common.Usuario import Usuario

def editar_perfil(valor_1,valor_2,valor_3):
    usuario = Usuario(valor_1,valor_2,valor_3)
    
    ruta=os.path.join(os.getcwd(),'data','json','usuarios_datos')
    try:
        arch_usuarios = open(ruta, "r+")
        datos_arch = json.load(arch_usuarios)
        exito,datos_arch = modificar(datos_arch,usuario)
        if exito:
            arch_usuarios.seek(0)
            json.dump(datos_arch, arch_usuarios,indent=4)
        arch_usuarios.close()    
        return exito
    except FileNotFoundError:
        return False
    

def modificar(datos_arch,usuario):
    """Devuelve True si el nick a ingresar existe y modifica los respectivos datos. 
    Caso contrario devuelve False"""
    
    for dato in datos_arch:
        if dato['nick']== usuario.nick:
            dato['edad'] = usuario.edad
            dato['genero'] = usuario.genero
            return True,datos_arch
    return False,datos_arch