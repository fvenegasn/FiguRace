import os
import json
from common.usuario import Usuario

def editar_perfil(nick:str,edad:str,genero:str,contraseña:str):
    """
        Edita los datos del perfil si el nick ingresado existe y la contraseña es correcta
    """
    
    usuario = Usuario(nick,edad,genero,contraseña)
    if (not edad.isnumeric()):
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
    """
    x = filter(
        lambda x: x['nick']==usuario.nick and x['contraseña'] == usuario.contraseña,datos_arch
        )

    usuario_buscado = list(x)
    exito = usuario_buscado !=[]

    if exito:
        usuario_buscado[0]['edad'] = usuario.edad
        usuario_buscado[0]['genero'] = usuario.genero

        datos_arch = list(
            filter(
            lambda x: x['nick']!=usuario.nick or x['contraseña'] != usuario.contraseña,datos_arch
            )
        )

        datos_arch.append(usuario_buscado[0])

    return exito,datos_arch