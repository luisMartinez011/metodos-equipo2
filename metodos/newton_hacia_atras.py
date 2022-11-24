import numpy as np
from random import randint
from metodos.metodos_padre import Metodo_Padre


class Newton_hacia_atras(Metodo_Padre):

    def __init__(self):
        selectProblem = randint(1, 2)
        if selectProblem == 1:
            self.x = np.array([2.2, 2.5, 2.8])
            self.y_values = np.array([2.54, 2.82, 3.21])
            self.value = 2.4
            self.problemImage = "Newton_hacia_atras_1.png"
        elif selectProblem == 2:
            self.x = np.array([1891, 1901, 1911, 1921, 1931])
            self.y_values = np.array([46, 66, 81, 93, 101])
            self.value = 2.4
            self.problemImage = "Newton_hacia_atras_2.png"
        self.selectProblem = selectProblem

    @staticmethod
    def formula():
        return "Newton_hacia_atras.png"

    # returns the method name
    @staticmethod
    def methodName():
        return "Newton hacia atras"

    def solve(self):
        x = self.x
        y_values = self.y_values
        value = self.value
        n = len(x)

        def u_cal(u, n):
            temp = u
            for i in range(1, n):
                temp = temp * (u + i)
            return temp

        # Calculating factorial of given n
        def fact(n):
            f = 1
            for i in range(2, n + 1):
                f *= i
            return f

        y = [[0.0 for _ in range(n)] for __ in range(n)]
        for i in range(n):
            y[i][0] = y_values[i]

        # Calculating the backward difference table
        for i in range(1, n):
            for j in range(n - 1, i - 1, -1):
                y[j][i] = y[j][i - 1] - y[j - 1][i - 1]

        # Initializing u and sum
        sum = y[n - 1][0]
        u = (value - x[n - 1]) / (x[1] - x[0])
        for i in range(1, n):
            sum = sum + (u_cal(u, i) * y[n - 1][i]) / fact(i)
        result = sum
