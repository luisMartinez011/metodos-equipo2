import numpy as np
from random import randint
from metodos.metodos_padre import Metodo_Padre


class Linea_recta:

    def __init__(self):
        selectProblem = randint(1, 2)
        self.x = x = np.array([1.1, 1.9, 2.4, 4.8, 5.1, 10.5])
        self.y = np.array([2.5, 2.7, 3.7, 5.2, 6.0, 8.3])
        self.problemImage = "Linea_recta_1.png"

    @staticmethod
    def formula():
        return "Linea_recta.png"

    @staticmethod
    def methodName():
        return "Linea recta"

    def solve(self):
        x = self.x
        y = self.y
        A = np.vstack([x, np.ones(len(x))]).T
        m, c = np.linalg.lstsq(A, y, rcond=None)[0]
        return m, c

    # override this method to generate two anser per option
    def generatePossibleSolutions(self, standard_deviation=0.5):
        a, b = self.solve()

        fake_solutions = 4

        rng = np.random.default_rng()
        s = rng.normal(a, standard_deviation, size=(fake_solutions, 2))
        s = np.append(s, [[a, b]], axis=0)
        rng.shuffle(s)
        return s
