import json
from typing import Any

def leer_json_data(name:str,encoding:str='utf8'):
    with open(name,encoding=encoding) as file:
        datos = json.load(file)
    return datos

def escribir_json_data(data:Any,name:str,enconding:str='utf8') -> None: 
    with open(name,"w",encoding=enconding) as file:
        json.dump(data,file,ensure_ascii=False,indent=4)