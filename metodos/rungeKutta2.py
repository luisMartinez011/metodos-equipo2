import numpy as np


class Runge_Kutta2:

    def __init__(self):
        self.y0 = 1
        self.t0 = 0
        self.h = 0.6
        
        self.x = 4

    # returns a formula´s string
    @staticmethod
    def formula():
        return "Runge_Kutta2.png"

    @staticmethod
    def methodName():
        return "Runge Kutta 2 Orden (RESULTADO DEL LIBRO INCORRECTO (k2)"

    def generatePossibleSolutions(self):
        solution = self.solve()
        # change this value if you want customized solutions
        # if your solution is an integer number, change this value to an integer
        standard_deviation = 0.1
        fake_solutions = 4

        rng = np.random.default_rng()
        s = rng.normal(solution, standard_deviation, fake_solutions)
        s = np.append(s, solution)
        rng.shuffle(s)
        return s



    # solves the problem
    def solve(self):

        k1 = self.h * ( (2* (self.y0 * self.t0)) -1  )
        k2 = self.h * ( (2 * (self.t0 + self.h) * (self.y0 + k1)) -1)
        y1 = self.y0 + (1/2 * (k1 + k2) ) 
	
        t1 = self.t0 + 1
	
        k12 = self.h * ( (2* (y1 * t1)) -1  )
        k22 = self.h * ( (2 * (t1 + self.h) * (y1 + k12)) -1)
        y2 = y1 + (1/2 * (k12 + k22) ) 

        g_x = y2

        self.g_x = g_x

        return g_x

    # return error margin
    def error(self):
        f_x = np.log(self.x)
        error = abs(f_x - self.g_x)

        return error
