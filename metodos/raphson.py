from random import randint
import pandas as pd
import numpy as np
import functools
import sympy as sp
from math import *


class Newton_Raphson:
    
    def __init__(self):
        self.tol = 10**(-5)
        self.x = 0
        selectProblem = randint(1, 2)
        if selectProblem == 1:
            self.x1 = 1
            self.indi = 1
            #self.problemImage = "Bisectriz_1"
        elif selectProblem == 2:
            self.self.x1 = 2
            self.indi = 2
            #self.problemImage = "Bisectriz_1"
        self.x1 = 0
        self.k = 0  
        self.n = 100    
    @staticmethod
    def formula():
        return "Raphson.png"

    @staticmethod
    def methodName():
        return "Newton Raphson"

    def f(self):
        #aqui van las funciones 
        print ('fuck')
    def df(self):
        #aqui va la derivada de la funcion
        print ('fuck')

    def solve(self):

        for self.k in range(self.n):
            self.x1 = self.x0-self.f(self.x0)/self.df(self.x0)
            if (abs(self.x1-self.x0) < self.tol):
                return self.x0, self.x1
            self.x0 = self.x1
            aux = abs(self.x1-self.x0)

    def error(self):
        ext = abs(self.x1-self.x0)
        return format(abs(self.x1-self.x0), '0.9f')
