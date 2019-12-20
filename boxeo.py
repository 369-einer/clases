class Boxeo():
    def __init__(self,clasificatorias,ubicacion,premios,hora):
        self.clasificatorias=clasificatorias
        self.ubicacion=ubicacion
        self.premios=premios
        self.hora=hora
    def ganar(self,ganar):
        self.ganar=ganar
    def setUbicacion(self):
        return self.ubicacion
    def perder(self,perder):
        self.perder=perder