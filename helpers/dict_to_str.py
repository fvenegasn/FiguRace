def procesar_eleccion (values: dict) -> str:
    """
    función 'procesar_eleccion'

    Def:
        Dado un diccionario pasado por parámetro, esta función devuelve la clave del elemento en el que su valor sea True
    
    Args:
        - values (dict): Diccionario con valores booleanos a procesar
    """
    for elem in values:
        if values[elem]:
            chosen_dataset = elem
    return chosen_dataset

##No usamos esta funcion