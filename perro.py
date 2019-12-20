class Perro():
    def __init__(self,color,velocidad_perro,tamaño,edad):
        self.color=color
        self.edad=edad
        self.velocidad_perro=velocidad_perro
        self.tamaño=tamaño
    def correr(self,correr):
        self.correr=correr
    def casar(self,casar):
        self.casar=casar
    def getVlocidad_gato(self):
        return self.velocidad_perro