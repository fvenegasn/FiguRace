from common.archivo import escribir_json_data,leer_json_data
from common.paths import ruta_usuarios_datos
from common.usuario import Usuario


def editar_perfil(nick:str,edad:str,genero:str):
    """
        Edita los datos del perfil si el nick ingresado existe
    """
    
    usuario = Usuario(nick,edad,genero,contraseña='0')
    if (not edad.isnumeric()):
        return False

    try:
        datos_arch = leer_json_data(ruta_usuarios_datos)
        exito,datos_arch = modificar(datos_arch,usuario)

        if exito:
            escribir_json_data(datos_arch,ruta_usuarios_datos)
        return exito

    except FileNotFoundError:
        return False
    

def modificar(datos_arch:list[dict],usuario:Usuario):
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