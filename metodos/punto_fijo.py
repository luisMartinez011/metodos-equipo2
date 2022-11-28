from random import randint
import pandas as pd
import numpy as np
import functools
from mpmath import *


class Punto_Fijo:

    def __init__(self):
        self.tol = 10**(-5)
        self.a = 0
        self.x = 0
        self.m = 0
        self.op = 0 
        selectProblem = randint(1, 3)
        if selectProblem == 1:
            self.problemImage = "pfijo1.png"
            self.op = 1
        elif selectProblem == 2:
            self.problemImage = "pfijo2.png"
            self.op = 2
        elif selectProblem == 3:
            self.problemImage = "pfijo3.png"
            self.op = 3


    def generatePossibleSolutions(self, standard_deviation = 0.1):
        a, b, e = self.solve()
        # change this value if you want customized solutions
        # (optional) if your solution is an integer number, change this value to an intege
        fake_solutions = 3

        rng = np.random.default_rng()
        s = rng.normal(a, standard_deviation, size=(fake_solutions,3))
        s = np.append(s, [[e,a,b]], axis= 0)
        rng.shuffle(s)
        return s


    @staticmethod
    def formula():
        return "Ayuda_PuntoFijo.png"

    @staticmethod
    def methodName():
        return "Punto Fijo"

    def solve(self):
        if self.op == 3:
            return 3.38760 , 0.98398 , 0.00004
        aux = 0
        if self.op == 1:
            self.m = (exp(self.a) - 2)
            self.m = round(self.m, 9)
        elif self.op == 2:
            self.m = (exp(self.a) - 2) / 2
            self.m = round(self.m, 9)
        k = 0
        while (abs(self.m-self.x) > self.tol):
            self.x = self.m
            self.a = self.m
            if self.op == 1:
                self.m = (exp(self.a) - 2)
                self.m = round(self.m, 9)
            elif self.op == 2:
                self.m = (exp(self.a) - 2) / 2
                self.m = round(self.m, 9)
            k = k+1
            
        error = round(self.m - self.x,9)
        a = round(self.x,9)
        b = round(self.m,9)
        return a , b , error   