#!/usr/bin/env python
# coding: utf-8

# In[1]:

import sys
sys.path.append("../") # go to parent dir


# # Importando Modelos

# In[2]:


from models.Vector import Vector, Coordenate
from models.Graphic import Graphic


# # Importando Librerias

# In[3]:


import numpy
import math


# # Ejercicio 1
# Sean los vectores A~ = 3i + 4j − 6k y B~ = −6i + 2j + 8k, encuentre gr´aficamente. Verifique que los resultados estan en un plano.

# In[4]:


A = Vector( value=Coordenate(3, 4, -6), label="A", color='r')
B = Vector(origin=A.destiny,value=Coordenate(-6,2,8), label="B", color='g')


# (a) R = A + B , |R|, sus cosenos directores cos α1 = Rx/R, cos α2 = Ry/R, cos α3 = Rz/R

# In[5]:


R = A+B
G = Graphic()
G.vector(A)
G.vector(B)
G.vector(R)
G.show()
print('A:{} + B:{} = R:{}'.format(A,B,R))
print('Longitud R = {}'.format(R.length))
print('Cos(a1) = {}'.format(R.value.x/R.length))
print('Cos(a2)= {}'.format(R.value.y/R.length))
print('Cos(a3) = {}'.format(R.value.z/R.length))


# (b) R = B + A

# In[6]:


B.setOrigin()
A.setOrigin(B.destiny)
R = B+A
G = Graphic()
G.vector(A)
G.vector(B)
G.vector(R)
G.show()
print('A:{} + B:{} = R:{}'.format(A,B,R))
print('Longitud R = {}'.format(R.length))
print('Cos(a1) = {}'.format(R.value.x/R.length))
print('Cos(a2) = {}'.format(R.value.y/R.length))
print('Cos(a3) = {}'.format(R.value.z/R.length))


# (c) S = 2A − 3B

# In[7]:


A.setOrigin()
A_2 = A.mulEscalar(2)
B_3 = B.mulEscalar(3)
#B_3.setOrigin(A_2.destiny)
S = A_2-B_3
G = Graphic()
G.vector(A)
G.vector(A_2)
G.vector(B)
G.vector(B_3)
G.vector(S)
G.show()
print('2*A:{} - 3*B:{} = S:{}'.format(A_2,B_3,S))
print('Longitud S = {}'.format(S.length))
print('Cos(a1) = {}'.format(S.value.x/S.length))
print('Cos(a2) = {}'.format(S.value.y/S.length))
print('Cos(a3) = {}'.format(S.value.z/S.length))


# (d) D = A − B

# In[8]:


A.setOrigin()
B.setOrigin(A.destiny)
D = A-B
G = Graphic()
G.vector(A)
G.vector(B)
G.vector(D)
G.show()
print('A:{} - B:{} = D:{}'.format(A,B,D))
print('Longitud D = {}'.format(D.length))
print('Cos(a1) = {}'.format(D.value.x/D.length))
print('Cos(a2) = {}'.format(D.value.y/D.length))
print('Cos(a3) = {}'.format(D.value.z/D.length))


# (e) D~ = B~ − A~

# In[9]:


B.setOrigin()
A.setOrigin(B.destiny)
D =B-A
G = Graphic()
G.vector(A)
G.vector(B)
G.vector(D)
G.show()
print('B:{} - A:{} = D:{}'.format(B,A,D))
print('Longitud D = {}'.format(D.length))
print('Cos(a1) = {}'.format(D.value.x/D.length))
print('Cos(a2) = {}'.format(D.value.y/D.length))
print('Cos(a3) = {}'.format(D.value.z/D.length))


# # Ejercicio 2
# Dibuje un pent´agono de lado 5 cm vectorialmente, hacer que cada lado del pent´agono sea un vector. Demuestre que la suma de dichos vectores es igual a cero.

# In[10]:


labels = ['u','v','w','a','b']

length = 5
u = Vector(value=Coordenate(math.cos(0)*length, math.cos(math.pi/2)*length, 0), label=labels.pop(), color=numpy.random.rand(3,) )
vectors = [u]
prev = 0
ang_inter = 108 # Angulo interno de un pentagono regular
last = u

G = Graphic(xmin=-3.5, xmax=6.5, ymin=-1.25, ymax = 8.75, zmin = -6.5, zmax = 3.5)
G.vector(u)

res = "{}: {}".format(last.label , last)
suma = last
while len(labels)!=0:
    ang_dec = prev + 180- ang_inter
    ang_rad = math.pi/180*ang_dec
    prev = ang_dec 
    cos_ang = math.cos(ang_rad)
    cos_comp_ang = math.cos(math.pi/2-ang_rad)
    new_x = cos_ang*length
    new_y = cos_comp_ang*length
    new_z = 0
    last = Vector(origin = last.destiny ,value =Coordenate(new_x, new_y, new_z), label=labels.pop(), color=numpy.random.rand(3,))
    vectors.append(last)
    
    G.vector(last)
    res = "{} + {}: {}".format(res ,last.label , last)
    suma = suma + last
    print("{} = {}".format(res, suma) )

    
G.show()



# # Ejercicio 3

# Graficar dicho pent´agono de lado 5 cm vectorialmente en 3 dimensiones, sabiendo que dicho
# pent´agono esta perpendicular con el plano xz y forma un ´angulo de 30◦ con el eje x. Demuestre que la suma de dichos vectores es igual a cero

# In[11]:




G = Graphic(xmin=-3.5, xmax=6.5, ymin=-1.25, ymax = 8.75, zmin = -6.5, zmax = 3.5)

res = "{}: {}".format(last.label , last)
suma = Vector()
origin = Coordenate(0,0,0)

#for vector in vectors:
    #G.vector(vector)
for vector in vectors:
    #G.vector(vector)
    print(vector.value)
    vector.rotateY(30)
    vector.setOrigin(origin) 
    origin = vector.destiny
    G.vector(vector)
    res = "{} + {}: {}".format(res ,vector.label , vector)
    suma = suma + vector
    print("{} = {}".format(res, suma) )
G.show()    


# # Ejercicio 4
# Sean los vectores A = 6i − 4j + 6k, B = −8i + 2j + 5k y C = 2i − 7j + 3k. Determine y grafique según corresponda.

# In[12]:


A = Vector(value=Coordenate(6,-4,6), label='A', color=numpy.random.rand(3,))
B = Vector(value=Coordenate(-8,2,5), label='B', color=numpy.random.rand(3,))
C = Vector(value=Coordenate(2,-7,3), label='C', color=numpy.random.rand(3,))


# (a) e = A · B y encuentre el ángulo entre estos vectores

# In[13]:


G = Graphic()
G.vector(A)
G.vector(B)
G.show()
e = A * B
radiands = A.angle(B)
grades =  radiands*180/math.pi
print("Producto Punto e = A * B:" , e)
print("Angulo: {} rad, {}°".format(radiands, grades))


# (b) R = (A · B )C

# In[14]:


R = C.mulEscalar(A * B)
G = Graphic()
G.vector(A)
G.vector(B)
G.vector(C)
G.vector(R)
G.show()
print("Producto Punto (A * B) C:" , R)


# (c) R = (A · B)C + (B · C)A

# In[15]:


R = C.mulEscalar(A * B)+ A.mulEscalar(B * C)
G = Graphic()
G.vector(A)
G.vector(B)
G.vector(C)
G.vector(R)
G.show()
print("Producto Punto (A * B) C + (B * C) A:" , R)


# (d) D = A ⊗ B

# In[16]:


D = A.productCrux(B, length=10)
D.setLabel('D')
G = Graphic()
G.vector(A)
G.vector(B)
G.vector(D)
G.show()
print("A ⊗ B = D:{}".format(D))


# (e) D = B x A

# In[17]:


D = B.productCrux(A)
D.setLabel('D')
G = Graphic()
G.vector(A)
G.vector(B)
G.vector(D.resize(10))
G.show()
print("B ⊗ A = D:{}".format(D))


# (f) D = (A ⊗ B) ⊗ C

# In[18]:


AXB = A.productCrux(B)
D = AXB.productCrux(C)
D.setLabel('D')
G = Graphic()
G.vector(A)
G.vector(B)
G.vector(C)
G.vector(D.resize(10))
G.vector(AXB.resize(10))
G.show()
print("(A ⊗ B) ⊗ C:{}".format(D))


# (g) D = A ⊗ (B ⊗ C)

# In[19]:


AXB = A.productCrux(B, length=10)
D = AXB.productCrux(C, length=10)
D.setLabel('D')
G = Graphic()
G.vector(A)
G.vector(B)
G.vector(C)
G.vector(D)
G.vector(AXB)
G.show()
print("(A ⊗ B) ⊗ C:{}".format(D))


# # Ejercicio 5

# Se ingresan dos vectores. Qué condición óptima aplica para que saber si los vectores son paralelos o perpendiculares?

# In[20]:


x1 = float(input("Ingrese coordenada X del Vector u:\t"))
y1 = float(input("Ingrese coordenada Y del Vector u:\t"))
z1 = float(input("Ingrese coordenada Z del Vector u:\t"))
u = Vector(
    value=Coordenate(
        x=x1,
        y=y1,
        z=z1
    ),
    label='u',
    color=numpy.random.rand(3, )
)

x2 = float(input("Ingrese dirección X del Vector v:\t"))
y2 = float(input("Ingrese dirección Y del Vector v:\t"))
z2 = float(input("Ingrese dirección Z del Vector v:\t"))
v = Vector(
    value=Coordenate(
        x=x2,
        y=y2,
        z=z2
    ),
    label='v',
    color=numpy.random.rand(3, )
)

G=Graphic()
G.vector(u)
G.vector(v)
G.show()
print("Son paralelos:\t{}\nSon perpendiculares:\t{}".format(u.areParallels(v), u.arePerpendicular(v)))


# In[ ]:




