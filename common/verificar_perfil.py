from encodings import utf_8
import os
import json
from common.guardar_perfil import existe


def verificar_perfil(nick,contraseña):

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

def guardar_seleccionado(nick):
    ruta=os.path.join(os.getcwd(),'data','txt','perfil_seleccionado.txt')
    with open(ruta,"w",encoding='utf-8') as arch_nombre:
        arch_nombre.write(nick)

def mostrar_seleccionado():
    ruta=os.path.join(os.getcwd(),'data','txt','perfil_seleccionado.txt')
    try:
        with open(ruta,"r",encoding='utf-8') as arch_nombre:
            return arch_nombre.read()
    except FileNotFoundError:
        return "No hay perfil seleccionado"