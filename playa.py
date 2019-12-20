class Playa():
    def __init__(self, arerna, ubicacion, temperatura):
        self.arerna = arerna
        self.ubicacion = ubicacion
        self.temperatura = temperatura

    def jugar(self, jugar):
        self.jugar = jugar

    def getTemperatura(self, temperatura):
        return self.temperatura
