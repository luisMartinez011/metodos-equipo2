import numpy as np
from metodos.metodos_padre import Metodo_Padre


class Polinomios:
    @staticmethod
    def formula():
        return "Polinomios.png"

    @staticmethod
    def methodName():
        return "Raices de Polinomios"

    def __init__(self):
        self.x = np.array([1, 1, -6])
        self.problemImage = "Polinomios1.png"

    def solve(self):
        self.x = np.poly1d(self.x)
        res = self.x.r
        return res

    # This method is an override from original generatePossibleSolutions function
    # This new function returns two solutions
    def generatePossibleSolutions(self, standard_deviation=0.5):
        a, b = self.solve()

        fake_solutions = 4

        rng = np.random.default_rng()
        s = rng.normal(a, standard_deviation, size=(fake_solutions, 2))
        s = np.append(s, [[a, b]], axis=0)
        rng.shuffle(s)
        return s
