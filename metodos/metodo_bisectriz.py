from random import randint
import pandas as pd
import numpy as np
import functools
import sympy as sp
from math import *
#from metodos.metodos_padre import Metodo_Padre


class Bisectriz():

    @staticmethod
    def methodName():
        return "Método Bisectriz"

    def __init__(self):
        self.m1 = 0
        self.k = 0
        self.m = 0
        self.x = 0
        self.tol = pow(10, -3)
        selectProblem = randint(1, 3)
        if selectProblem == 1:
            self.a = 0
            self.b = 1
            self.accion = 1
            self.problemImage = "Bisectriz_1.png"
            self.op = 1
        elif selectProblem == 2:
             self.op = 2
             self.a = -5
             self.b = 14
             self.formulaElegida = 2
             self.problemImage = "Bisectriz_2.png"
        elif selectProblem == 3:
            self.problemImage = "Bisectriz_3.png"
            self.op = 3
            

    @staticmethod
    def formula():
        return "Bisectriz.png"

    def generatePossibleSolutions(self):
        a,b,e = self.solve()
        # change this value if you want customized solutions
        # if your solution is an integer number, change this value to an integer
        standard_deviation = 0.5
        fake_solutions = 3

        rng = np.random.default_rng()
        s = rng.normal(a, standard_deviation, size=(fake_solutions, 3))
        s = np.append(s, [[a, b, e]], axis=0)
        rng.shuffle(s)
        return s

    #def extra(x,self):
        # definir formulas
            #return pow(x, 3) - 6.5*x + 2

    def solve(self):
        
        if self.op == 3:
            return 0.7333984375 , 0.73291015625 , 0.00048828
        
        self.m1 = self.a
        self.m = self.b
        self.k = 0
        while (abs(self.m1 - self.m) > self.tol):
            self.m1 = self.m
            self.m = (self.a + self.b) / 2

            if self.op == 1:
                auxa= pow(self.a, 3) - 6.5*self.a + 2
                auxb= pow(self.b, 3) - 6.5*self.b + 2
                auxm = pow(self.m, 3) - 6.5*self.m + 2
            elif self.op == 2:
                auxa= pow(self.a, 3) - 4*pow(self.a,2) - 10
                auxb= pow(self.b, 3) - 4*pow(self.a,2) - 10
                auxm = pow(self.m, 3) - 4*pow(self.a,2) - 10

            if (auxa * auxm < 0):  # cambia el singo en este intervalos
                self.b = self.m
            if (auxm  * auxb < 0):  # cambia el signo en este intervalo
                self.a = self.m
            self.k = self.k + 1
        # devuelve el intervalo
        retornoa = self.a
        retornob = self.b
        error = self.error()
        return retornoa, retornob , error

    def error(self):
        error = self.m1 - self.m
        return error
