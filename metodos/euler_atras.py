import numpy as np
import sympy as sp
from random import randint
from metodos.metodos_padre import Metodo_Padre


class Euler_Atras(Metodo_Padre):

    def __init__(self):
        self.problemImage = "Euler_Atras_1.png"

    @staticmethod
    def formula():
        return "Euler_Atras.png"

    @staticmethod
    def methodName():
        return "Euler hacia atras"

    def solve(self):
        t0, tf = 0.5
        n = 5
        h = (tf-t0)/n
        s0, k, k1, km, E = 200, 13.7, 80, 15, 3
        emax = 0.001

        def f(a):
            z = (a**3)+(a**2)*(k1+km)-(k1*si)+a * \
                ((k1*km)-(k1*si)-(km*si)+(k*E*k1*h))-(si*k1*km)
            return z

        def fp(a):
            z = mpmath.diff(f, a)
            return z

        t = np.linspace(t0, tf, n+1)
        s = np.zeros(n+1)
        s[0] = s0

        for i in range(n):
            a = s[i]
            e = 2*emax
            si = s[i]
            while e > emax:
                an = a-(f(a)/fp(a))
                e = abs((an-a)/an)*100
                a = an
            s[i+1] = a

        return s
#print("De acuerdo al método euler atras: ", s)
