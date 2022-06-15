from common.archivo import leer_json_data
from common.paths import ruta_usuarios_datos

def verificar_perfil(nick:str,contraseña:str):
    """
        Devuelve True si existe el nick y la contraseña es correcta.
        Caso contrario devuelve False
    """
    try:
        datos_arch= leer_json_data(ruta_usuarios_datos)
        x = filter(lambda x: x['nick']==nick and x['contraseña'] == contraseña,datos_arch)
        return list(x)

    except FileNotFoundError:
        return False
