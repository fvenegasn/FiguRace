from common.paths import ruta_configuracion,ruta_usuarios_datos
from common.archivo import escribir_json_data, leer_json_data
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
    
    
    exito = False
    try:
        datos_arch = leer_json_data(ruta_usuarios_datos)
        
        #Me fijo si el nick ya existe
        nick = dato_in['nick']
        if not existe(datos_arch,nick):
            exito = True
            datos_arch.append(dato_in)
            escribir_json_data(datos_arch,ruta_usuarios_datos)

    except FileNotFoundError:
        exito = True
        escribir_json_data([dato_in],ruta_usuarios_datos)

    return exito

def existe(datos_arch:list,nick:str):
   
    """
        Devuelve True si el nick a ingresar ya existe. 
        Caso contrario devuelve False
    """
    
    x = filter(lambda x: x['nick']==nick,datos_arch)

    return list(x)

