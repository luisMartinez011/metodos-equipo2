from random import randint
import pandas as pd
import numpy as np
import functools
import sympy as sp
from math import *


class Newton_Raphson:
    def generatePossibleSolutions(self):
        solution = self.solve()
        # change this value if you want customized solutions
        # (optional) if your solution is an integer number, change this value to an integer
        standard_deviation = 0.5
        fake_solutions = 4

        rng = np.random.default_rng()
        s = rng.normal(solution, standard_deviation, fake_solutions)
        s = np.append(s, solution)
        rng.shuffle(s)
        return s
        
    def __init__(self):
        self.tol = 10**(-5)
        self.x = 0
        self.x1 = 1
        self.indi = 1
        self.problemImage = "rapson1.png"
        self.x1 = 0
        self.k = 0  
        self.n = 100    
    @staticmethod
    def formula():
        return "Raphson.png"

    @staticmethod
    def methodName():
        return "Newton Raphson"

    def f(self,x):
        #aqui van las funciones 
        x = 0.8*pow(x,2) + x - 3
        return x
    def df(self,dx):
        #aqui va la derivada de la funcion
        dx = (1.6* dx) +1 
        return dx

    def solve(self):

        for self.k in range(self.n):
            self.x1 = self.x0-self.f(self.x0)/self.df(self.x0)
            if (abs(self.x1-self.x0) < self.tol):
                return self.x1 #self.x0,
            self.x0 = self.x1
            aux = format(abs(self.x1-self.x0), '0.9f')
            return aux

    def error(self):
        ext = abs(self.x1-self.x0)
        return format(abs(self.x1-self.x0), '0.9f')
