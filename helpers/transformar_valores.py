#Esta función pasa los valores ingresados en pantalla por el usuario a la configuración del juego


def values_to_options(parametros:dict, values:dict, difficulty:str) -> None:
    """
    función 'values_to_options'

    Def:
        Modifica el diccionario con los parámetros de configuración actuales con los valores
        ingresados por el usuario en pantalla.
    
    Args:
        - options (dict): Diccionario que contiene los parámetros de juego para cada dificultad
        - values (dict): Diccionario que contiene los parámetros de juego ingresado por el usuario en pantalla
        - difficulty (str): String que contiene la dificultad elegida por el usuario en pantalla
    """
    
    son_numeros = list(filter(lambda x: x!='' and x.isnumeric(),values.values()))

    if (len(son_numeros) == len(values)):
        
        claves = parametros[difficulty].keys()

        actualizado = dict(zip(claves,values.values()))

        parametros[difficulty].update(actualizado)
