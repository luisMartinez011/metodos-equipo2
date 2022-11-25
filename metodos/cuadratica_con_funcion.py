import numpy as np
from random import randint


class Cuadratica_con_funcion:

    def __init__(self):
        selectProblem = randint(1, 2)
        if selectProblem == 1:
            self.x = np.array([1.1, 1.9, 2.4, 4.8, 5.1, 10.5])
            self.y = np.array([2.5, 2.7, 3.7, 5.2, 6.0, 8.3])
            self.problemImage = "Cuadratica_1.png"
        elif selectProblem == 2:
            self.x = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5,
                              5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5])
            self.y = np.array([10.08, 12.03, 11.38, 18.81, 20.53, 28.5, 31.38, 38.4, 48.39,
                               60.6, 66.66, 82.61, 91.37,
                               105.44, 122.53, 137.77, 152.74, 172.65, 188.84, 207.77,
                               230.94, 251.35, 274.07, 295.95])
            self.problemImage = "Cuadratica_con_funcion_2.png"
        self.selectProblem = selectProblem

    @staticmethod
    def formula():
        return "Cuadratica_con_funcion.png"

    @staticmethod
    def methodName():
        return "Cuadratica con funcion"

    def solve(self):
        x = self.x
        y = self.y
        a, b, c = np.poly1d(np.polyfit(x,
                                       y, 2))
        c = c * np.exp(c)
        # result(set x value)
        return a, b, c

    def generatePossibleSolutions(self, standard_deviation=0.5):
        a, b, c = self.solve()

        fake_solutions = 4

        rng = np.random.default_rng()
        s = rng.normal(a, standard_deviation, size=(fake_solutions, 3))
        s = np.append(s, [[a, b, c]], axis=0)
        rng.shuffle(s)
        return s
