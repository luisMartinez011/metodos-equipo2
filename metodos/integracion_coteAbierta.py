import numpy as np

class Integracion_cotasAbiertas():

    def __init__(self):
        self.a = -2
        self.b = 2
        self.n = 4
        self.ah = (6/20)
        self.h = ((self.b - self.a)/(self.n + 2))

        self.x = 4
        self.problemImage = "CotesAbiertas2.png"
    
    def generatePossibleSolutions(self, standard_deviation=0.5):
        solution,a = self.solve()

        fake_solutions = 3

        rng = np.random.default_rng()
        s = rng.normal(solution, standard_deviation, size=(fake_solutions,2))
        s = np.append(s,[[solution , a]], axis=0)
        rng.shuffle(s)
        return s
    # returns a formula´s string
    @staticmethod
    def formula():
        return "CotesAbiertas.png"

    @staticmethod
    def methodName():
        return "Integración_cotasAbiertas"

    # solves the problem
    def solve(self):

        ValorI = (self.h) * (self.ah)
        f_a = (0 * ((3*(self.a)**3)-10))
        f_b = (0 * ((3*(self.b)**3)-10))

        f_h1 = (11 * ((3 * (self.a + (self.h*1))**3) - 10))
        f_h2 = (-14 * ((3 * (self.a + (self.h*2))**3) - 10))
        f_h3 = (26 * ((3 * (self.a + (self.h*3))**3) - 10))
        f_h4 = (-14 * ((3 * (self.a + (self.h*4))**3) - 10))
        f_h5 = (11 * ((3 * (self.a + (self.h*5))**3) - 10))

        f_suma = (f_h1 + f_h2 + f_h3 + f_h4 + f_h5)

        g_x = ValorI * (f_a + f_b + f_suma)

        self.g_x = g_x

        return g_x,f_h5
