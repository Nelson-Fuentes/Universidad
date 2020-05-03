from models.Vector import Vector, Coordenate
from models.Graphic import Graphic

def main():
    A = Vector( value=Coordenate(3, 4, -6), label="A", color='r')

    B = Vector(origin=A.destiny, value=Coordenate(-6, 2, 8), label="B", color='g')

    R = A+B
    G = Graphic()
    G.vector(A)
    G.vector(B)
    G.vector(R)
    G.show()



if __name__ == '__main__':
    main()

