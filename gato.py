class Gato():
    def __init__(self,color,edad,velocidad_gato,longitud):
        self.color=color
        self.edad=edad
        self.velocidad_gato=velocidad_gato
        self.longitud=longitud
    def correr(self,correr):
        self.correr=correr
    def casar(self,casar):
        self.casar=casar
    def getVlocidad_gato(self):
        return self.velocidad_gato