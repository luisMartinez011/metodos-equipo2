import numpy as np


class Runge_Kutta4_38:

    def __init__(self):
        self.y0 = 1
        self.t0 = 0
        self.h = 0.5

        self.x = 4
        self.problemImage = "Runge_Kutta4_382.png"
    # returns a formula´s string

    @staticmethod
    def formula():
        return "Runge_Kutta4_38.png"

    @staticmethod
    def methodName():
        return "Runge Kutta 4: 3/8 Simpson"

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

        k1 = self.h * ((-self.y0) / (((self.y0)**2) + self.t0))
        k2 = self.h * (((-self.y0) + (k1/3)) /
                       ((((self.y0)+(k1/3))**2) + ((self.t0) + (self.h/3))))
        k3 = self.h * (((-self.y0) + (k1/3) + (k2)) /
                       ((((self.y0)+(k1/3)+(k2/3))**2) + (self.t0 + ((2/3)*self.h))))
        k4 = self.h * (((-self.y0) + (k1) - (k2) + (k3)) /
                       ((((self.y0) + (k1) - (k2) + (k3))**2) + (self.t0 + self.h)))

        y1 = self.y0 + ((1/8) * (k1 + (3*k2) + (3*k3) + k4))

        t1 = self.t0 + 1

        k12 = self.h * ((-y1) / (((y1)**2) + t1))
        k22 = self.h * (((-y1) + (k12/3)) /
                        ((((y1)+(k12/3))**2) + ((t1) + (self.h/3))))
        k32 = self.h * (((-y1) + (k12/3) + (k22)) /
                        ((((y1)+(k12/3)+(k22/3))**2) + (t1 + ((2/3)*self.h))))
        k42 = self.h * (((-y1) + (k12) - (k22) + (k32)) /
                        ((((y1 + (k12) - (k22) + (k32))**2) + (t1 + self.h))))

        y2 = y1 + ((1/8) * (k12 + (3*k22) + (3*k32) + k42))

        g_x = y1

        self.g_x = g_x

        return g_x
