class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return "color {} y ruedas {}".format(self.color, self.ruedas)

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + ", velocidad {} y cc {}".format(self.velocidad, self.cilindrada)
    
class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return super().__str__() + ", carga {}".format(self.carga)

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    
    def __str__(self):
        return super().__str__() + ", tipo {}".format(self.tipo)
    
class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return super().__str__() + ", velocidad {} y cc {}".format(self.velocidad, self.cilindrada)

vehiculos = [
    Coche("Azul", 4, 150, 80000),
    Camioneta("Blanco", 4, 150000, 1300, 150),
    Bicicleta("Verde", 2, "Urbano"),
    Motocicleta("Gris", 2, "Deportiva", 2500, 250)
]

def catalogar(vehiculos):
    for v in vehiculos:
        print("{} {}".format(type(v).__name__, v))

catalogar(vehiculos)

def catalogar2(vehiculos, ruedas = None):
    
    if ruedas != None:
        contador = 0
        for n in vehiculos:
            if n.ruedas == ruedas:
                contador += 1
        print("Se han encontrado {} vehiculos con {}".format(contador, ruedas))
    
    for v in vehiculos:
        if ruedas == None:
            print("{} {}".format(type(v).__name__, v))
        elif v.ruedas == ruedas:
            print("{} {}".format(type(v).__name__, v))

catalogar2(vehiculos, 2)