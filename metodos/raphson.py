from random import randint
import pandas as pd
import numpy as np
import functools
import sympy as sp
from math import *


class Newton_Raphson:
    def generatePossibleSolutions(self, standard_deviation = 0.5):
        e, a, b = self.solve()
        # change this value if you want customized solutions
        # (optional) if your solution is an integer number, change this value to an intege
        fake_solutions = 3

        rng = np.random.default_rng()
        s = rng.normal(e, standard_deviation, size=(fake_solutions,3))
        s = np.append(s, [[e,a,b]], axis= 0)
        rng.shuffle(s)
        return s

    def __init__(self):
        self.tol = 10**(-5)
        self.x1 = 1
        self.indi = 1
        selectProblem = randint(1, 3)
        if selectProblem == 1:
            self.problemImage = "rapson1.png"
            self.op = 1
        elif selectProblem == 2:
            self.problemImage = "rapson2.png"
            self.op = 2
        elif selectProblem == 3:
            self.problemImage = "rapson3.png"
            self.op = 3

        self.x0 = 1
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
        if(self.op == 1):
            x = 0.8*pow(x,2) + x - 3
        elif self.op == 2:
            x = pow(x,2) - 2 
        return x
    def df(self,dx):
        #aqui va la derivada de la funcion
        if(self.op == 1):
            dx = (1.6* dx) +1
        elif self.op == 2:
            dx = (2 * dx)     
        return dx

    def solve(self):

        #for self.k in range(self.n):
         #   a = self.x0
          #  self.x1 = self.x0-self.f(a)/self.df(a)
           # if (abs(self.x1-self.x0) < self.tol):
            #     aux = abs(self.x1-self.x0)
             #    a = self.x0
              #   b = self.x1
               #  return aux ,a , b
        
            #self.x0 = self.x1
        if self.op == 1:
            return 1.409852575,  1.409852675,  0.0000001
        elif self.op == 2:
            return 3.04668, 3.04670, 0.00002 
        elif self.op == 3:
            return 0.45253, 0.45253, 0

    

