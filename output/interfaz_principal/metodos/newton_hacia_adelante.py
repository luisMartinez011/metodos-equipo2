import numpy as np
from random import randint
from metodos.metodos_padre import Metodo_Padre


class Newton_hacia_adelante(Metodo_Padre):

    def __init__(self):
        selectProblem = randint(1, 2)
        if selectProblem == 1:
            self.x = np.array([2.2, 2.5, 2.8])
            self.y_values = np.array([2.54, 2.82, 3.21])
            self.value = 2.4
            self.problemImage = "Newton_hacia_adelante_1.png"
        elif selectProblem == 2:
            x = np.array([45, 50, 55, 60])
            self.x = x
            self.y_values = np.sin(np.deg2rad(x))
            self.value = 52
            self.problemImage = "Newton_hacia_adelante_2.png"
        self.selectProblem = selectProblem

    @staticmethod
    def formula():
        return "Newton_hacia_adelante.png"

    @staticmethod
    def methodName():
        return "Newton hacia adelante"

    def solve(self):
        x = self.x
        n = len(x)

        def u_cal(u, n):

            temp = u
            for i in range(1, n):
                temp = temp * (u - i)
            return temp

        def fact(n):
            f = 1
            for i in range(2, n + 1):
                f *= i
            return f

        y = [[0 for i in range(n)]
             for j in range(n)]

        for i in range(n):
            y[i][0] = self.y_values[i]

        for i in range(1, n):
            for j in range(n - i):
                y[j][i] = y[j + 1][i - 1] - y[j][i - 1]

        # Displaying the forward difference table
        # for i in range(n):
        # 	print(x[i], end = "\t");
        # 	for j in range(n - i):
        # 		print(y[i][j], end = "\t");
        # 	print("");

        # initializing u and sum
        sum = y[0][0]
        u = (self.value - x[0]) / (x[1] - x[0])
        for i in range(1, n):
            sum = sum + (u_cal(u, i) * y[0][i]) / fact(i)

        result = sum
        return result
