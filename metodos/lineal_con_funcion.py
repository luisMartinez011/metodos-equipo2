import numpy as np
from random import randint
from metodos.metodos_padre import Metodo_Padre


class Lineal_con_funcion(Metodo_Padre):

    def __init__(self):
        selectProblem = randint(1, 2)
        if selectProblem == 1:
            self.x = np.array([2.2, 2.5, 2.8])
            self.y = np.array([2.54, 2.82, 3.21])
            self.xi = 2.4
            self.problemImage = "Lineal_con_funcion_1.png"
        elif selectProblem == 2:
            self.x = np.array([1, -3, 5, 7])
            self.y = np.array([-2, 1, 2, -3])
            self.xi = 2
            self.problemImage = "Lineal_con_funcion_2.png"
        self.selectProblem = selectProblem

    @staticmethod
    def formula():
        return "Lineal_con_funcion.png"

    @staticmethod
    def methodName():
        return "Lineal con funcion"

    def solve(self):
        poly = lagrange(self.x, self.y)
        result = np.round(poly(self.xi), 9)
        return result
