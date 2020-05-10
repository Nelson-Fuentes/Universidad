import math

import numpy


class Coordenate:
    DEFAULT_X = 0
    DEFAULT_Y = 0
    DEFAULT_Z = 0

    def __init__(self, x=DEFAULT_X, y=DEFAULT_Y, z=DEFAULT_X):
        self.__x__ = x
        self.__y__ = y
        self.__z__ = z

    @property
    def x(self):
        return self.__x__

    @property
    def y(self):
        return self.__y__

    def __add__(self, other):
        return Coordenate(x=self.__x__ + other.__x__, y=self.__y__ + other.__y__, z=self.__z__ + other.__z__)

    def __sub__(self, other):
        return Coordenate(x=self.__x__ - other.__x__, y=self.__y__ - other.__y__, z=self.__z__ - other.__z__)

    @property
    def z(self):
        return self.__z__

    def mulEscalar(self, number):
        return Coordenate(x=self.x * number, z=self.z * number, y=self.y * number)

    def __str__(self):
        return '({}, {}, {})'.format(self.__x__, self.__y__, self.__z__)


class Vector:
    DEFAULT_ORIGIN = Coordenate()
    DEFAULT_VALUE = Coordenate()
    DEFAULT_LABEL = "v"
    DEFAULT_COLOR = "b"

    def __init__(self, origin=DEFAULT_ORIGIN, value=DEFAULT_VALUE, label=DEFAULT_LABEL, color=DEFAULT_COLOR):
        self.__origin__ = origin
        self.__value__ = value
        self.__label__ = label
        self.__color__ = color

    def __add__(self, other):
        return Vector(origin=self.origin, value=self.value + other.value, color=numpy.random.rand(3, ),
                      label='({}) + ({})'.format(self.label, other.label))

    def __sub__(self, other):
        return Vector(origin=self.origin, value=self.value - other.value, color=numpy.random.rand(3, ),
                      label='({}) - ({})'.format(self.label, other.label))

    def setOrigin(self, origen=Coordenate()):
        self.__origin__ = origen

    def setLabel(self, label):
        self.__label__ = label

    @property
    def color(self):
        return self.__color__

    @property
    def label(self):
        return self.__label__

    @property
    def origin(self):
        return self.__origin__

    @property
    def destiny(self):
        return self.origin + self.value

    @property
    def value(self):
        return self.__value__

    @property
    def x(self):
        return self.__value__.__x__

    @property
    def z(self):
        return self.__value__.__z__

    @property
    def y(self):
        return self.__value__.__y__


    @property
    def length(self):
        return float(math.sqrt(self.value.x ** 2 + self.value.y ** 2 + self.value.z ** 2))

    def mulEscalar(self, number):
        return Vector(origin=self.origin, value=self.value.mulEscalar(number),
                      label=str(number) + '*(' + self.label + ')', color=numpy.random.rand(3, ))

    def __str__(self):
        return "[{}; {}; {}]".format("{:.2f}".format(self.value.x), "{:.2f}".format(self.value.y),
                                     "{:.2f}".format(self.value.z))

    def __matrixRotationZ(self, radians):
        return [
            [math.cos(radians), -1 * math.sin(radians), 0],
            [math.sin(radians), math.cos(radians), 0],
            [0, 0, 1]
        ]

    def __matrixRotationY(self, radians):
        return [
            [math.cos(radians), 0, math.sin(radians)],
            [0, 1, 0],
            [-1 * math.sin(radians), 0, math.cos(radians)]]

    def __matrixRotationX(self, radians):
        return [
            [1, 0, 0],
            [0, math.cos(radians), -1 * math.sin(radians)],
            [0, math.sin(radians), math.cos(radians)]]

    def list(self):
        return [[ self.value.x ],[ self.value.y],[self.value.z ]]

    def rotateZ(self, grades):
        radians = grades*math.pi/180
        self.__rotate__(self.__matrixRotationZ(radians))

    def rotateY(self, grades):
        radians = grades * math.pi / 180
        self.__rotate__(self.__matrixRotationY(radians))

    def rotateX(self, grades):
        radians = grades * math.pi / 180
        self.__rotate__(self.__matrixRotationX(radians))

    def __rotate__(self, matrix):
        array = numpy.dot(matrix, self.list())
        x, y, z = numpy.transpose(array).tolist()[0]
        length = self.length
        self.__value__ = Coordenate(x, y, z)

    def __mul__(self, vector):
        return self.value.x * vector.value.x + self.value.y * vector.value.y + self.value.z * vector.value.z

    def angle(self, vector):
        return float(math.acos((self * vector)/(self.length * vector.length)))

    def productCrux(self, vector, length = None):
        label = "({}) ⊗ ({})".format(self.label, vector.label)
        crux = Vector(
            value=Coordenate(
                x=self.value.y * vector.value.z - self.value.z * vector.value.y,
                y=self.value.z * vector.value.x - self.value.x * vector.value.z,
                z=self.value.x * vector.value.y - self.value.y * vector.value.x),
            label=label,
            color=numpy.random.rand(3, )
        )
        if length is not None:
            crux_resize = crux.resize(length)
            crux_resize.setLabel(label)
            return crux_resize
        else:
            return crux

    def unitaryVector(self):
        length = self.length
        return Vector(
            value=Coordenate(
                x=self.value.x/length,
                y=self.value.y/length,
                z=self.value.z/length,
            ),
            label="unitary({})".format(self.label),
            color=numpy.random.rand(3, )
        )

    def resize(self, length):
        new_vector = self.unitaryVector()
        new_vector.__value__ = Coordenate(
            x=new_vector.value.x*length,
            y=new_vector.value.y*length,
            z=new_vector.value.z*length
        )
        new_vector.setLabel("resize from ({}) length: {}".format(self.label, length))
        return new_vector

    def areParallels(self, vector):
        try:
            dx = self.value.x  / vector.value.x
            dy = self.value.y / vector.value.y
            dz = self.value.z / vector.value.z
            return dx == dy and dx == dz
        except:
            return False

    def arePerpendicular(self, vector):
        return self * vector == 0
