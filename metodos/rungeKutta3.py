import numpy as np


class Runge_Kutta3:

    def __init__(self):
        self.y0 = 1
        self.t0 = 0
        self.h = 0.25

        self.x = 4
        self.problemImage = "Runge_Kutta32.png"

    # returns a formula´s string
    @staticmethod
    def formula():
        return "Runge_Kutta3.png"

    @staticmethod
    def methodName():
        return "Runge Kutta 3 Orden"

    def generatePossibleSolutions(self):
        solution = self.solve()
        # change this value if you want customized solutions
        # if your solution is an integer number, change this value to an integer
        standard_deviation = 0.1
        fake_solutions = 3

        rng = np.random.default_rng()
        s = rng.normal(solution, standard_deviation, fake_solutions)
        s = np.append(s, solution)
        rng.shuffle(s)
        return s

    # solves the problem

    def solve(self):

        k1 = self.h * (((2 * (self.y0 * self.t0)) + 1) / ((self.y0)**2))
        k2 = self.h * (((2 * (self.y0 + (k1/2)) * (self.t0 +
                       (self.h/2))) + 1) / ((self.y0 + (self.h / 2))**2))
        k3 = self.h * (((2 * ((self.y0 - k1) + (2*(k2))) *
                       (self.t0 + self.h)) + 1) / ((self.y0 - self.h) + 2 * (k2))**2)

        y1 = self.y0 + ((1/6) * (k1 + (4 * k2) + k3))

        t1 = self.t0 + 1

        k12 = self.h * (((2 * (y1 * t1)) + 1) / ((y1)**2))
        k22 = self.h * \
            (((2 * (y1 + (k12/2)) * (t1 + (self.h/2))) + 1) / ((y1 + (self.h / 2))**2))
        k32 = self.h * (((2 * ((y1 - k12) + (2*(k22))) *
                        (t1 + self.h)) + 1) / ((y1 - self.h) + 2 * (k22))**2)

        y2 = y1 + ((1/6) * (k12 + (4 * k22) + k32))

        g_x = y2

        self.g_x = g_x
        return g_x
