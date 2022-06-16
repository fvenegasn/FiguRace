from random import choices
import string

def generar_random_string(cant)->str:
    return ''.join(choices(string.ascii_lowercase + string.digits, k = cant))

def gen_id():
    id_partida = (
        generar_random_string(8) + '-' + generar_random_string(4) + '-' 
        + generar_random_string(4) + '-' + generar_random_string(16)
    )
    return id_partida