import numpy as np
from random import randint
from metodos.metodos_padre import Metodo_Padre


class Newton_Diferencias_Divididas(Metodo_Padre):

    def __init__(self):
        selectProblem = randint(1, 2)
        if selectProblem == 1:
            self.x = np.array([4.4, 3.7, 3.1])
            self.y = np.array([-0.68, -1.59, -1.82])
            self.xi = 3.5
            self.problemImage = "Newton_Diferencias_Divididas_1.png"
        elif selectProblem == 2:
            self.x = np.array([-5, -1, 0, 2])
            self.y = np.array([-2, 6, 1, 3])
            self.xi = 2.1
            self.problemImage = "Newton_Diferencias_Divididas_2.png"
        self.selectProblem = selectProblem

    @staticmethod
    def formula():
        return "Newton_Diferencias_Divididas.png"

    @staticmethod
    def methodName():
        return "Newton con diferencias divididas"

    def solve(self):
        def divided_diff(x, y):
            n = len(y)
            coef = np.zeros([n, n])
            # the first column is y
            coef[:, 0] = y

            for j in range(1, n):
                for i in range(n-j):
                    coef[i][j] = \
                        (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j]-x[i])

            return coef

        def newton_poly(coef, x_data, x):
            n = len(x_data) - 1
            p = coef[n]
            for k in range(1, n+1):
                p = coef[n-k] + (x - x_data[n-k])*p
            return p

        a_s = divided_diff(self.x, self.y)[0, :]
        result = newton_poly(a_s, self.x, self.xi)

        return result
