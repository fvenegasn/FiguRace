def procesar_eleccion (values):
    for elem in values:
        if values[elem]:
            chosen_dataset = elem
    return chosen_dataset