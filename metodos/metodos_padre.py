import numpy as np
from random import randint


class Metodo_Padre:

    # change standar_deviation value if you want customized solutions
    # if your solution is an integer number, change standard deviation to an integer
    def generatePossibleSolutions(self, standard_deviation=0.5):
        solution = self.solve()

        fake_solutions = 4

        rng = np.random.default_rng()
        s = rng.normal(solution, standard_deviation, fake_solutions)
        s = np.append(s, solution)
        rng.shuffle(s)
        return s
