class Agricultor():
    def __init__(self,nombre,edad,horas_detrabjo,sembrio):
        self.nombre=nombre
        self.edad=edad
        self.horas_detrabjo=horas_detrabjo
        self.sembrio=sembrio
    def trabajar(self,trabajar):
        self.trabajar=trabajar
    def sembrar(self,sembrar):
        self.sembrar=sembrar
    def getNombre(self,nombre):
        return self.nombre

