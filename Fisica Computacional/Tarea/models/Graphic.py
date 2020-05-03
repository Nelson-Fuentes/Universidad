import matplotlib.pyplot as plt
from .Vector import Vector
import numpy as np
from mpl_toolkits.mplot3d import axes3d
from IPython import display, Math, Latex

class Graphic:

    DEFAULT_X_MIN = -10
    DEFAULT_X_MAX = 10
    DEFAULT_Y_MIN = -10
    DEFAULT_Y_MAX = 10
    DEFAULT_Z_MIN = -10
    DEFAULT_Z_MAX = 10


    def __init__(self, xmin=DEFAULT_X_MIN, xmax=DEFAULT_X_MAX, ymin=DEFAULT_Y_MIN, ymax = DEFAULT_Y_MAX, zmin = DEFAULT_Z_MIN, zmax = DEFAULT_Z_MAX):
        self.__figure__ = plt.figure()
        self.__axis__ = self.__figure__.gca(projection='3d')
        self.__axis__.set(xlim=(xmin, xmax), ylim=(ymin, ymax), zlim=(zmin,zmax), xlabel='Eje X', ylabel='Eje Y', zlabel='Eje Z')

    def vector(self, v: Vector):
        self.__axis__.text((v.destiny.x + v.origin.x) / 2, (v.destiny.y + v.origin.y) / 2, (v.destiny.z + v.origin.z) / 2, v.label, color=v.color)
        return  self.__axis__.quiver(v.origin.x, v.origin.y, v.origin.z, v.value.x, v.value.y, v.value.z, color=v.color)

    def show(self):
        plt.show()
