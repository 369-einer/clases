class Cliente():
    def __init__(self,dis_dinero,nombre,identidad,trabajo):
        self.dis_dinero=dis_dinero
        self.nombre=nombre
        self.identidad=identidad
        self.trabajo=trabajo
    def pagar(self,pagar):
        self.pagar=pagar
    def setDis_dinero(self):
        return self.dis_dinero
    def getIdentidad(self):
        return self.identidad