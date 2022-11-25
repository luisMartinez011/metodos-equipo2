import numpy as np
from random import randint


class Interpolacion_lineal:

    def __init__(self):
        selectProblem = randint(1, 2)
        if selectProblem == 1:
            self.a = 2
            self.b = 5
            self.x = 4
            self.problemImage = "Interpolacion_lineal_1.png"
        elif selectProblem == 2:
            self.a = 3
            self.b = 5
            self.x = 4
            self.problemImage = "Interpolacion_lineal_2.png"
        self.selectProblem = selectProblem

    # returns the direction of the formula image
    @staticmethod
    def formula():
        return "Interpolacion_lineal.png"

    @staticmethod
    def methodName():
        return "Interpolación lineal"

    # returns an array with 4 fake solutions and the real solution

    def generatePossibleSolutions(self, standard_deviation=0.5):
        a, b = self.solve()

        fake_solutions = 3

        rng = np.random.default_rng()
        s = rng.normal(a, standard_deviation, size=(fake_solutions, 2))
        s = np.append(s, [[a, b]], axis=0)
        rng.shuffle(s)
        return s
    # solves the problem

    def solve(self):
        f_a = np.log(self.a)
        f_b = np.log(self.b)
        g_x = (((f_b - f_a) / (self.b-self.a)) * (self.x-self.a)) + f_a
        self.g_x = g_x
        error = self.error()
        return g_x, error

    # return error margin
    # some problems may not have this method
    def error(self):
        f_x = np.log(self.x)
        error = abs(f_x - self.g_x)

        return error
