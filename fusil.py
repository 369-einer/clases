class Fusil():
    def  __init__(self,calibre,tiempo_dedisparo,lisencia):
        self.calibre=calibre
        self.tiempo_dedisparo=tiempo_dedisparo
        self.lisencia=lisencia
    def disparar(self,disparar):
        self.disparar=disparar
    def getLisencia(self):
        return  self.lisencia

