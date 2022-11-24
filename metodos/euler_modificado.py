import numpy as np
import sympy as sp
import functools
from random import randint
from math import *

class Euler_Modificado:
    @staticmethod
    def formula():
        return "/Euler_Modificado.png"

    @staticmethod
    def methodName():
        return "EulerModificado"
    
def generatePossibleSolutions(self):
        solution = self.solve()
        # change this value if you want customized solutions
        # (optional) if your solution is an integer number, change this value to an integer
        standard_deviation = 0.5
        fake_solutions = 4

def f(t,y):
    func=t*exp(3*t)-2*y
    return func 

def eulermod(t,y,h,n):
    print('y(',t,')=',y)
    for k in range(n):
        y0=y+h*f(t,y)
        y=y+(h/2)*(f(t,y)+f(t+h,y0))
        t=t+h
        print('y(',t,')=',y)
        
eulermod(0,1.2,0.3,2)
