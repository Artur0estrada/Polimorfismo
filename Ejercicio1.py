class Figura:
    def calcularArea(self):
        return 0

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def calcularArea(self):
        return 3.1416 * (self.radio * self.radio)

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcularArea(self):
        return self.base * self.altura

circulo = Circulo(5)
rectangulo = Rectangulo(4, 6)

print("Área del círculo:", circulo.calcularArea())
print("Área del rectángulo:", rectangulo.calcularArea())
