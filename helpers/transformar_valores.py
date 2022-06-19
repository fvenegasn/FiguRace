
def values_to_options(parametros:dict, valores_ingresados:dict, difficulty:str) -> bool:
    """
    función 'values_to_options'

    Def:
        Modifica el diccionario con los parámetros de configuración actuales con los valores
        ingresados por el usuario en pantalla.
    
    Args:
        - parametros (dict): Diccionario que contiene los parámetros de juego para cada dificultad
        - values (dict): Diccionario que contiene los parámetros de juego ingresado por el usuario en pantalla
        - difficulty (str): String que contiene la dificultad elegida por el usuario en pantalla
    """
    
    son_numeros = list(filter(lambda x: x!='' and x.isnumeric(),valores_ingresados.values()))
    exito = len(son_numeros) == len(valores_ingresados)
    if exito:
        
        claves = parametros[difficulty].keys()
        string_a_entero = map(lambda x: int(x), valores_ingresados.values())

        actualizado = dict(zip(claves,string_a_entero))
        
        parametros[difficulty].update(actualizado)
    return exito