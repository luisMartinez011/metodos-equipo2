import numpy as np
from scipy.interpolate import lagrange
from random import randint
from metodos.metodos_padre import Metodo_Padre


class Lagrange(Metodo_Padre):

    def __init__(self):
        selectProblem = randint(1, 2)
        if selectProblem == 1:
            self.x = np.array([2.2, 2.5, 2.8])
            self.y = np.array([2.54, 2.82, 3.21])
            self.xi = 2.4
            self.problemImage = "Lagrange_1.png"
        elif selectProblem == 2:
            self.x = np.array([-3, 1, 5, 7])
            self.y = np.array([-4, -2, 1, 2])
            self.xi = 2
            self.problemImage = "Lagrange_2.png"
        self.selectProblem = selectProblem

    @staticmethod
    def formula():
        return "Lagrange.png"

    @staticmethod
    def methodName():
        return "Lagrange"

    def solve(self):
        poly = lagrange(self.x, self.y)
        result = np.round(poly(self.xi), 9)
        return result
