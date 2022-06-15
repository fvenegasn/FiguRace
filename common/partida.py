import random

class Partida():

    def __init__(self,id_partida, evento, usuarie,estado,texto_ingresado,respuesta,nivel):

        self._id = id_partida
        self._timestamp = random.randrange(1000000000,9999999999)
        self._evento = evento
        self._usuarie = usuarie
        self._estado = estado
        self._texto_ingresado = texto_ingresado
        self._respuesta = respuesta
        self._nivel = nivel