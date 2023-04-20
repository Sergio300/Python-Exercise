import math

class Punto () :
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({},{})".format(self.x, self.y)
    
    def cuadrante(self):
        if self.x > 0  and self.y > 0:
            print("{} pertenece al primer cuadrante".format(self))
        elif self.x < 0  and self.y > 0:
            print("{} pertenece al seguno cuadrante".format(self))
        elif self.x < 0  and self.y < 0:
            print("{} pertenece al tercer cuadrante".format(self))
        elif self.x > 0  and self.y < 0:
            print("{} pertenece al cuarto cuadrante".format(self))
        else:
            print("{} Se encuentra sobre el origen".format(self))

    def vector(self, punto ):
        print("El vector entre {} y {} es ({},{})".format(self, punto, punto.x - self.x, punto.y - self.y))
    
    def distancia (self, punto):
        d = math.sqrt((punto.x - self.x)**2 + (punto.y - self.y)**2)
        print("La distancia entre los puntos {} y {} es {}".format(self, punto, d ))

class Rectangulo():
    def __init__(self, pI = Punto(), pF = Punto()):
        self.pI = pI
        self.pF = pF

    def base(self):
        self.base = abs(self.pF.x - self.pI.x)
        print("La base es {}".format(self.base))

    def altura(self):
        self.altura = abs(self.pF.y - self.pI.y)
        print("La altura es {}".format(self.altura))

    def area(self):
        self.base = abs(self.pF.x - self.pI.x)
        self.altura = abs(self.pF.y - self.pI.y)
        self.area = self.base * self.altura
        print("El area es {}".format(self.area))


        

A = Punto(2,3)
B = Punto(5,5)
C = Punto(-3,-1)
D = Punto(0,0)

A.cuadrante()
C.cuadrante()
D.cuadrante()

A.vector(B)
B.vector(A)

A.distancia(B)
B.distancia(A)

A.distancia(D)
B.distancia(D)
C.distancia(D)

R = Rectangulo(A,B)
R.base()
R.altura()
R.area()




