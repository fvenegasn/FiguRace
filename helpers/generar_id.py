from random import choices
import string

def generar_random_string(cant:int)->str:
    """
        Retorna de forma aleatoria una cadena de caracteres de longitud 'cant', 
        formada por números y letras minúsculas.
    """
    return ''.join(choices(string.ascii_lowercase + string.digits, k = cant))

def gen_id()->str:
    """
        Genera de forma aleatoria un id de partida.
    """
    id_partida = (
        generar_random_string(8) + '-' + generar_random_string(4) + '-' 
        + generar_random_string(4) + '-' + generar_random_string(16)
    )
    return id_partida