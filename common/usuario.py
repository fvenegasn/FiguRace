class Usuario():
    
    def __init__(self,nick,edad,genero,contraseña):
        self._nick = nick
        self._edad = edad
        self._genero = genero
        self._contraseña = contraseña
        self._puntaje = {"Facil":0,"Media":0,"Dificil":0}
    
    def generar_dicci(self):
        return {
            "nick": self._nick, 
            "edad": self._edad,
            "genero": self._genero,
            "contraseña": self._contraseña,
            "puntaje": self._puntaje,
        }
    
    @property
    def nick(self):
        return self._nick
    
    @nick.setter
    def nick(self,value):
        self._nick = value
    
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self,value):
        self._edad = value

    @property
    def genero(self):
        return self._genero
    
    @genero.setter
    def genero(self,value):
        self._genero = value

    @property
    def contraseña(self):
        return self._contraseña
    
    @contraseña.setter
    def contraseña(self,value):
        self._contraseña = value
    
    @property
    def puntaje(self):
        return self._puntaje

    @puntaje.setter
    def puntaje(self,value):
        self._puntaje = value