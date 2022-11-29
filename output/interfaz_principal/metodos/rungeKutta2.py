import numpy as np


class Runge_Kutta2:

    def __init__(self):
        self.y0 = 1
        self.t0 = 0
        self.h = 0.6

        self.x = 4
        self.problemImage = "Runge_Kutta22.png"

    # returns a formula´s string
    @staticmethod
    def formula():
        return "Runge_Kutta2.png"

    @staticmethod
    def methodName():
        return "Runge Kutta 2 Orden"


    # solves the problem

    def solve(self):

        k1 = self.h * ((2 * (self.y0 * self.t0)) - 1)
        k2 = self.h * ((2 * (self.t0 + self.h) * (self.y0 + k1)) - 1)
        y1 = self.y0 + (1/2 * (k1 + k2))

        t1 = self.t0 + 1

        k12 = self.h * ((2 * (y1 * t1)) - 1)
        k22 = self.h * ((2 * (t1 + self.h) * (y1 + k12)) - 1)
        y2 = y1 + (1/2 * (k12 + k22))

        g_x = y2

        self.g_x = g_x

        return y1,g_x

    def generatePossibleSolutions(self, standard_deviation=0.5):
        a, b = self.solve()

        fake_solutions = 3

        rng = np.random.default_rng()
        s = rng.normal(a, standard_deviation, size=(fake_solutions, 2))
        s = np.append(s, [[a, b]], axis=0)
        rng.shuffle(s)
        return s
