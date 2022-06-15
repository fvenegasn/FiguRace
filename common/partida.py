import random

class Partida():

    def __init__(self,timestamp,id_partida, evento, usuarie,estado,texto_ingresado,respuesta,nivel):

        self._id = id_partida
        self._timestamp = timestamp
        self._evento = evento
        self._usuarie = usuarie
        self._estado = estado
        self._texto_ingresado = texto_ingresado
        self._respuesta = respuesta
        self._nivel = nivel