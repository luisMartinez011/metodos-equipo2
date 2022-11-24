from random import randint
import pandas as pd
import numpy as np
import functools
from math import *


class Punto_Fijo:

    def __init__(self):
        self.tol = 10**(-5)
        self.a = 0
        self.x = 0
        self.m = 0
        selectProblem = randint(1, 2)

    @staticmethod
    def formula():
        return "Ayuda_PuntoFijo.png"

    @staticmethod
    def methodName():
        return "Punto Fijo"

    def func(self):
        return exp(-self.x)

    def solve(self):
        aux = 0
        self.m = self.func(self.a)
        k = 0
        while (abs(self.a-self.m) > self.tol):
            self.a = self.m
            aux = self.m
            self.m = self.func(self.a)
            k = k+1
        error = self.error()
        return error

    def error(self):
        e = self.a - self.m
        return abs(e)
