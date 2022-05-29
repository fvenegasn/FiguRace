#Esta función pasa los valores ingresados en pantalla por el usuario a la configuración del juego
from common.validar_numeros import validate_integer


def values_to_options(options_copy:dict, values:dict, difficulty:str) -> None:
    """
    función 'values_to_options'

    Def:
        Modifica el diccionario con los parámetros de configuración predeterminado con los valores
        ingresados por el usuario en pantalla.
    
    Args:
        - options (dict): Diccionario que contiene los parámetros de juego para cada dificultad
        - values (dict): Diccionario que contiene los parámetros de juego ingresado por el usuario en pantalla
        - difficulty (str): String que contiene la dificultad elegida por el usuario en pantalla
    """
    x = 0

    for elem in options_copy[difficulty]:
        if (values[x] != "" and validate_integer(values[x])):
            options_copy[difficulty][elem] = int(values[x])
        x = x + 1
