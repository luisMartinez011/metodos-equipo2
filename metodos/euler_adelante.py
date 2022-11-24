import numpy as np
import sympy as sp
from random import randint
from metodos.metodos_padre import Metodo_Padre


class Euler_Adelante(Metodo_Padre):

    def __init__(self):
        self.problemImage = "Euler_Adelante_1.png"

    @staticmethod
    def formula():
        return "Euler_Adelante.png"

    @staticmethod
    def methodName():
        return "Euler hacia adelante"

    def solve(self):
        t0, tf = 0.5
        n = 5
        h = (tf-t0)/n
        s0, k, k1, km, E = 200, 13.7, 80, 15, 3
        emax = 0.001
        t = np.linspace(t0, tf, n+1)
        s1 = np.zeros(n+1)
        s1[0] = s0
        for i in range(n):
            si = s1[i]
            a = ((-(k*E*k1)/(k1+si))*((si)/(km+si)))*h+si
            s1[i+1] = a
        return s1
#print("De acuerdo al metodo euler hacia adelante: ", s1)
