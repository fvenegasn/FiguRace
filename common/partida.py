class Partida():

    def __init__(self,timestamp,id_partida, evento, usuarie,estado,texto_ingresado,respuesta,nivel,genero, dataset):

        self._id = id_partida
        self._timestamp = timestamp
        self._evento = evento
        self._usuarie = usuarie
        self._estado = estado
        self._texto_ingresado = texto_ingresado
        self._respuesta = respuesta
        self._nivel = nivel
        self._genero = genero
        self._dataset = dataset

    def devolver_valores(self):
        return {
            'Timestamp': self._timestamp,
            'Id': self._id,
            'Evento': self._evento,
            'Usuarie': self._usuarie,
            'Estado': self._estado,
            'Texto Ingresado': self._texto_ingresado,
            'Respuesta': self._respuesta,
            'Nivel': self._nivel,
            'Genero': self._genero,
            'Dataset': self._dataset
        }

    @property
    def id_partida(self):
        return self.id_partida

    @property
    def timestamp(self):
        return self._timestamp 
        
    @property
    def evento(self):
        return self._evento

    @property
    def usuarie(self):
        return self._usuarie

    @property
    def estado(self):
        return self._estado

    @property
    def texto_ingresado(self):
        return self._texto_ingresado
        
    @property
    def respuesta(self):
        return self.respuesta

    @property
    def nivel(self):
        return self._nivel

    @property
    def genero(self):
        return self._genero
        