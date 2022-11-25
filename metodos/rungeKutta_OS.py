import numpy as np


class Runge_Kutta_OS:

    def __init__(self):
        self.a = 2
        self.b = 1
        self.Vny0 = 1.2
        self.Uny0 = 1.1
        self.qnt0 = 0
        self.h = 0.2

        self.x = 4
        self.problemImage = "Runge_Kutta_OS2.png"

    # returns a formula´s string
    @staticmethod
    def formula():
        return "Runge_Kutta_OS.png"

    @staticmethod
    def methodName():
        return "Runge Kutta Orden Superior"

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
        k1 = self.h * (self.Vny0)
        m1 = self.h * ((2 * self.Vny0 * self.qnt0) - self.Uny0)
        k2 = self.h * ((self.Vny0) + m1)
        m2 = self.h * ((self.a * (self.Vny0 + m1) *
                       (self.qnt0 + self.h)) - (self.b * (self.Uny0 + k1)))

        y1 = self.Uny0 + ((1/2) * (k1 + k2))
        y1p = self.Vny0 + ((1/2) * (m1 + m2))

        t1 = self.qnt0 + 1

        k12 = self.h * (y1p)
        m12 = self.h * ((2 * y1p * t1) - y1)
        k22 = self.h * ((y1p) + m12)
        m22 = self.h * ((self.a * (y1p + m12) * (t1 + self.h)
                         ) - (self.b * (y1 + k12)))

        y12 = y1 + ((1/2) * (k12 + k22))
        y12p = y1p + ((1/2) * (m12 + m22))

        g_x = y1p

        self.g_x = g_x

        return g_x
