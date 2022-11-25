from random import randint
import numpy as np
import sympy as sp
from math import *


class Falsa_Posicion:

    def __init__(self):
        self.cont = 0
        self.x = 0
        selectProblem = randint(1,2)
        if selectProblem == 1:
            self.a = 1
            self.b = 2
            self.fa = -5
            self.fb = 14
            self.problemImage = "fposicion2.png"
            self.op =1
        elif selectProblem == 2:
            self.a = 1
            self.b = 2
            self.fa = - 7.281718172
            self.fb = 4.778112190
            self.problemImage = "fposicion1.png"
            self.op = 2

        self.tol = 0.001
        self.e = 0
        self.eaux = 0

    @staticmethod
    def formula():
        return "FPosicion.png"

    @staticmethod
    def methodName():
        return "Falsa Posicion"


    def solve(self):
        if self.op == 1:
                #self.fa = (3*pow(self.a, 3)) - (2*self.a) - 3
                self.fa = pow(self.a,3) + (4 * pow(self.a,2)) -10
        elif self.op == 2:
                self.fa = self.a* exp(self.a) - 10 
        self.x = self.a - ((self.fa * (self.b - self.a)) / (self.fb - self.fa))   
            # Cambia el valor de a por el valor de x para el siguiente intervalo  
        while abs(self.x - self.a) > self.tol:
            self.a = self.x
            if self.op == 1:
                #self.fa = (3*pow(self.a, 3)) - (2*self.a) - 3
                self.fa = pow(self.a,3) + (4 * pow(self.a,2)) -10
            elif self.op == 2:
                self.fa = self.a * exp(self.a) - 10 
            self.x = self.a - ((self.fa * (self.b - self.a)) / (self.fb - self.fa))
            # Cambia el valor de a por el valor de x para el siguiente intervalo
            self.eaux = self.a
            print("xxxxxxx", (self.x - self.eaux), "xxxxxxx")
       
        e = self.x - self.eaux
        a= self.eaux
        b = self.x
        return a,b,e

    def generatePossibleSolutions(self, standard_deviation = 0.1):
            a, b, e = self.solve()
            # change this value if you want customized solutions
            # (optional) if your solution is an integer number, change this value to an intege
            fake_solutions = 3

            rng = np.random.default_rng()
            s = rng.normal(a, standard_deviation, size=(fake_solutions,3))
            s = np.append(s, [[a,b,e]], axis= 0)
            rng.shuffle(s)
            return s


