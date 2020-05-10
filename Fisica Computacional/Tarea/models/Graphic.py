import matplotlib.pyplot as plt
import numpy

from .Vector import Vector, Coordenate
import numpy as np
from mpl_toolkits.mplot3d import axes3d

class Graphic():
    DEFAULT_X_MIN = -10
    DEFAULT_X_MAX = 10
    DEFAULT_Y_MIN = -10
    DEFAULT_Y_MAX = 10

    def __init__(self, xmin=DEFAULT_X_MIN, xmax=DEFAULT_X_MAX, ymin=DEFAULT_Y_MIN, ymax=DEFAULT_Y_MAX, xlabel='Eje X', ylabel = 'Eje Y'):
        self.__figure__ = plt.figure()
        self.__axis__ = self.__figure__.gca()
        self.__axis__.set(xlim=(xmin, xmax), ylim=(ymin, ymax), xlabel=xlabel, ylabel=ylabel)

    def vector(self, v: Vector):
        self.__axis__.text((v.destiny.x + v.origin.x) / 2, (v.destiny.y + v.origin.y) / 2, v.label, color=v.color)
        return self.__axis__.quiver(v.origin.x, v.origin.y, v.value.x, v.value.y, color=v.color)

    def point(self, c: Coordenate):
        self.__axis__.plot(c.x, c.y, c.x, c.y)

    def show(self):
        plt.show(self.__figure__)


class Graphic3D(Graphic):

    DEFAULT_X_MIN = -10
    DEFAULT_X_MAX = 10
    DEFAULT_Y_MIN = -10
    DEFAULT_Y_MAX = 10
    DEFAULT_Z_MIN = -10
    DEFAULT_Z_MAX = 10


    def __init__(self, xmin=DEFAULT_X_MIN, xmax=DEFAULT_X_MAX, ymin=DEFAULT_Y_MIN, ymax = DEFAULT_Y_MAX, zmin = DEFAULT_Z_MIN, zmax = DEFAULT_Z_MAX, xlabel='Eje X', ylabel = 'Eje Y', zlabel = 'Eje Z'):
        self.__figure__ = plt.figure()
        self.__axis__ = self.__figure__.gca(projection='3d')
        self.__axis__.set(xlim=(xmin, xmax), ylim=(ymin, ymax), zlim=(zmin,zmax), xlabel=xlabel, ylabel=ylabel, zlabel=zlabel)

    def vector(self, v: Vector):
        self.__axis__.text((v.destiny.x + v.origin.x) / 2, (v.destiny.y + v.origin.y) / 2, (v.destiny.z + v.origin.z) / 2, v.label, color=v.color)
        return  self.__axis__.quiver(v.origin.x, v.origin.y, v.origin.z, v.value.x, v.value.y, v.value.z, color=v.color)

    def show(self):
        plt.show(self.__figure__)

    def point(self, c :Coordenate):
        self.__axis__.plot(xs=[c.x], ys=[c.y], zs=[c.z], color= numpy.random.rand(3, ), marker='o')