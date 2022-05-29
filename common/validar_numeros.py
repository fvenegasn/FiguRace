def validate_integer (num:str) -> bool:
    """
    funcion 'validate_integer'

    Def:
        Esta función retornará si el string pasado por parámetro es un número o no.

    Args:
        - num (str): Número a validar
    """
    return num.isnumeric()