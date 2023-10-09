class Animal:
    def mover(self):
        print("Movimiento genérico")

class Perro(Animal):
    def mover(self):
        print("Correr")

class Pez(Animal):
    def mover(self):
        print("Nadar")

class Pajaro(Animal):
    def mover(self):
        print("Volar")

perro = Perro()
pez = Pez()
pajaro = Pajaro()

perro.mover()
pez.mover()
pajaro.mover()
