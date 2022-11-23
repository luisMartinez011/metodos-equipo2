from random import randint
import pandas as pd
import numpy as np
import functools
import sympy as sp
from math import *


class Bisectriz:
    def __init__(self):
        self.m1 = 0
        self.k = 0
        self.m = 0
        self.x = 0
        self.tol = pow(10, -3)
        selectProblem = randint(1, 2)
        if selectProblem == 1:
            self.a = 0
            self.b = 1
            self.formula = 1
            self.problemImage = "Bisectriz_1"
        elif selectProblem == 2:
            self.a = 0
            self.b = 1
            self.formula = 2
            self.problemImage = "Bisectriz_2"
                

    def generatePossibleSolutions(self):
        solution = self.solve()
        # change this value if you want customized solutions
        # if your solution is an integer number, change this value to an integer
        standard_deviation = 0.5
        fake_solutions = 4

        rng = np.random.default_rng()
        s = rng.normal(solution, standard_deviation, fake_solutions)
        s = np.append(s, solution)
        rng.shuffle(s)
        return s

    @staticmethod
    def extra(self, x):
        #definir formulas
        if self.formula == 1: 
            return cos(x) - pow(x,3);
        else: 
            return pow(x,3) - 6.5*x + 2; 

    @staticmethod
    def formula():
        return "Bisectriz.png"

    @staticmethod
    def methodName():
        return "Metodo Bisectriz"

    def solve(self):
        self.m1 = self.a
        self.m = self.b
        self.k = 0
        while(abs(self.m1 - self.m) > self.tol):
            self.m1 = self.m
            self.m = (self.a + self.b) / 2;
            if(self.extra(self.a)* self.extra(self.m) < 0): #cambia el singo en este intervalos
                self.b = self.m
            if(self.extra(self.m)* self.extra(self.b) < 0): #cambia el signo en este intervalo   
                self.a = self.m
            self.k = self.k + 1;
        #devuelve el intervalo
        return self.a , self.b

    def error(self):
        error = format(self.m1 - self.m)
        return error
