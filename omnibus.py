class Omnibus():
    def __init__(self,nro_asientos,nombre,velocidad_maxima):
        self.nro_asientos=nro_asientos
        self.nombre=nombre
        self.velocidad_maxima=velocidad_maxima
    def transportar(self,transportar):
        self.transportar=transportar
    def getNombre(self,nombre):
        return self.nombre