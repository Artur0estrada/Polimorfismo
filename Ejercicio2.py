class Fruta:
    def obtenerColor(self):
        return "desconocido"

class Manzana(Fruta):
    def obtenerColor(self):
        return "rojo"

class Platano(Fruta):
    def obtenerColor(self):
        return "amarillo"

fruta1 = Manzana()
fruta2 = Platano()

print("Color de la Manzana:", fruta1.obtenerColor())
print("Color del Platano:", fruta2.obtenerColor())
