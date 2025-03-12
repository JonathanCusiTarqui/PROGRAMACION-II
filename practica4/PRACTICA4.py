import math
class FiguraGeometrica:
    def __init__(self,figura,*arg):
        self.figura=figura
        if figura == "circulo":
            self.radio = arg[0]
        elif figura == "rectangulo":
            self.base = arg[0]
            self.altura = arg[1]
        elif figura == "triangulo_rectangulo":
            self.base = arg[0]
            self.altura = arg[1]
        elif figura == "trapecio":
            self.basemayor = arg[0]
            self.basemenor = arg[1]
            self.altura = arg[2]
        elif figura == "pentagono":
            self.lado = arg[0]
            self.apotema = arg[1]
        
    def area(self):
        if self.figura == "circulo":
            # A = pi * r^2
            return math.pi * self.radio ** 2
        elif self.figura == "rectangulo":
            # A = base * altura
            return self.base * self.altura
        elif self.figura == "triangulo_rectangulo":
            # A = (base * altura) / 2
            return (self.base * self.altura) / 2
        elif self.figura == "trapecio":
            # A = (basemayor + basemenor) * h / 2
            return (self.basemayor + self.basemenor) * self.altura / 2
        elif self.figura == "pentagono":
            # A = (5 * lado * a) / 2
            return (5 * self.lado * self.apotema) / 2
        else:
            return "Figura no reconocida"
        
    def __str__(self):
        return f"{self.area()}"


resultado= FiguraGeometrica("pentagono",65,3)
print(resultado)


