import numpy as np


class Runge_Kutta4_13:

    def __init__(self):
        self.y0 = 0.4
        self.t0 = 0
        self.h = 0.2

        self.x = 4
        self.problemImage = "Runge_Kutta4_132.png"

    # returns a formula´s string
    @staticmethod
    def formula():
        return "Runge_Kutta4_13.png"

    @staticmethod
    def methodName():
        return "Runge Kutta 4: 1/3 Simpson"

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
        k1 = self.h * ((self.y0 + self.t0) ** 2 / (1 - self.y0))
        k2 = self.h * (((self.y0 + (k1/2)) + (self.t0 + (self.h/2)))
                       ** 2 / (1 - (self.y0 + (k1/2))))
        k3 = self.h * (((self.y0 + (k2/2)) + (self.t0 + (self.h/2)))
                       ** 2 / (1 - (self.y0 + (k2/2))))
        k4 = self.h * (((self.y0) + (k3) + (self.t0 + (self.h)))
                       ** 2 / (1 - (self.y0 + (k3))))

        y1 = (self.y0) + ((1/6) * (k1 + (2 * k2) + (2 * k3) + k4))

        t1 = self.t0 + 1

        k12 = self.h * ((y1 + t1) ** 2 / (1 - y1))
        k22 = self.h * (((y1 + (k12/2)) + (t1 + (self.h/2)))
                        ** 2 / (1 - (y1 + (k12/2))))
        k32 = self.h * (((y1 + (k22/2)) + (t1 + (self.h/2)))
                        ** 2 / (1 - (y1 + (k22/2))))
        k42 = self.h * (((y1) + (k32) + (t1 + (self.h)))
                        ** 2 / (1 - (y1 + (k32))))

        y2 = (y1) + ((1/6) * (k12 + (2 * k22) + (2 * k32) + k42))
        g_x = y1

        self.g_x = g_x

        return g_x
