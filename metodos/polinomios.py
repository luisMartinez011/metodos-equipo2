import numpy as np

class Polinomios:
    @staticmethod
    def formula():
        return "Polinomios.png"

    @staticmethod
    def methodName():
        return "Raices de Polinomios"
    def __init__(self):
        self.x = np.array([1 , 1 , -6])
        self.problemImage = "Polinomios.png"

    def solve(self):
        self.x = np.poly1d(self.x)
        res = self.x.r
        return res

    def generatePossibleSolutions(self):
        solution = self.solve()
        # change this value if you want customized solutions
        # (optional) if your solution is an integer number, change this value to an integer
        standard_deviation = 2
        fake_solutions = 4

        rng = np.random.default_rng()
        for i in range(solution):
            s = rng.normal(solution[i], standard_deviation, fake_solutions)
        s = np.append(s, solution)
        rng.shuffle(s)
        return s