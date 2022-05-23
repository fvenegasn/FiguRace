class Usuario():
    
    def __init__(self,nick,edad,genero):
        self._nick = nick
        self._edad = edad
        self._genero = genero
    
    def generar_dicci(self):
        return {
            "nick": self._nick, 
            "edad": self._edad,
            "genero": self._genero
        }
    

    def nick(self):
        return self._nick
    
    def nick(self,value):
        self._nick = value

    def edad(self):
        return self._edad
    
    def edad(self,value):
        self._edad = value

    def genero(self):
        return self._genero
    
    def genero(self,value):
        self._genero = value
