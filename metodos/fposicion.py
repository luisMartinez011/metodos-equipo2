import numpy as np
import sympy as sp
from math import *


class Falsa_Posicion:

    def __init__(self):
        self.cont = 0
        self.x = 0
        self.a = 1
        self.b = 2
        self.fa = -2
        self.fb = 17
        self.tol = 0.001
        self.e = 0
        self.eaux = 0

    @staticmethod
    def formula():
        return "FPosicion.png"

    @staticmethod
    def methodName():
        return "Falsa Posicion"

    def funcx(self):
        # Funcion que evalula la funcion x formula de la falsa-posicion
        self.x = self.a - ((self.fa * (self.b - self.a)) / (self.fb - self.fa))

    def funca(self):
        # Funcion que evuala la funcion F(a)
        self.fa = (3*pow(self.a, 3)) - 2*self.a - 3

    def ferro(self):
        # Funcion que cacula el error entre los dos intervalos
        error = self.eaux - self.e
        return error

    def solve(self):
        while abs(self.eaux - self.e) > self.tol:
            self.cont = self.cont + 1
            self.funca()
            self.funcx()
            aux = self.ferro()
            self.e = self.eaux
            self.eaux = aux
            # Cambia el valor de a por el valor de x para el siguiente intervalo
            self.a = self.x
            # A este punto deberia imprimir el intervalo final donde se encontro el error estimado
            #print('i' + self.cont + 'A = ' + self.a + 'F(a) = ' + self.funca() + 'Error = ' + self.eaux() + 'Error = ' + self.eaux)
            ayuda = self.eaux
            return ayuda

    def error(self):
        auxiliares = self.eaux
        return auxiliares


test = Falsa_Posicion()
test.solve()
