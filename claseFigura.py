class Figura(object):

    def calcularArea(self,area):

        self.area=area


class Rectangulo(Figura):

    def __init__(self,base,altura):
        self.base=base
        self.altura=altura



    def calcularArea(self,base,altura,area):
        area=base*altura

        return area

class Triangulo(Figura):

    def __init__(self,base,altura):
        self.base=base
        self.altura=altura

    def calcularArea(self,area,base,altura):
        area=(base*altura)/2

        return area

class Circulo(Figura):
    def __init__(self,radio):


        self.radio=radio

    def calcularArea(self,area,radio):
        pi = 3.1416
        area=pi*radio*radio

rectangulo=Rectangulo(5,6)
rectangulo.calcularArea(5,6,8)



