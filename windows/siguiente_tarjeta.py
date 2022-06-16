from common.hacer_ventana import crear_ventana
import time

def initialize(data):
    data["ronda"] = data["ronda"] + 1
    data["tiempo_inicial"] = time.time()

"""-------------------------EJECUCIÓN------------------------------"""
def ejecutar():
    from windows.jugar import interfaz,logistica
    layout,respuesta = interfaz()
    crear_ventana("Pantalla de Juego", layout,logistica,initialize=initialize,respuesta=respuesta)