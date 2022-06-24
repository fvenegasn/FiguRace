import json
from typing import Any

def leer_json_data(name:str,encoding:str='utf8')-> Any:
    """
        Devuelve los datos leídos del archivo jason ubicado en la ruta 'name'
    """
    with open(name,encoding=encoding) as file:
        datos = json.load(file)
    return datos

def escribir_json_data(data:Any,name:str,encoding:str='utf8') -> None:
    """
        Sobreescribe archivo jason ubicado en la ruta 'name' con los datos 'data'
    """ 
    with open(name,"w",encoding=encoding) as file:
        json.dump(data,file,ensure_ascii=False,indent=4)