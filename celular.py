class Celular():
    def __init__(self,año_fabricaion,modelo,marca):
        self.año_fabricaion=año_fabricaion
        self.modelo=modelo
        self.marca=marca
    def llamar(self,llamar):
        self.llamar=llamar
    def getMarca(self):
        return self.marca