import numpy as np
import random

class Montante:
    @staticmethod
    @staticmethod
    def formula():
        return "/Montante.png"

    @staticmethod
    def methodName():
        return "Montante"

    def __init__(self):
        selectProblem = random.randint(1, 2)
        if selectProblem == 1:
            self.problemImage = "Montante1.png"
            self.op = 1
        elif selectProblem == 2:
            self.problemImage = "Montante1.png"
            self.op = 2


    def solve(self):
            if(self.op == 1):
                a = 62/87
                b = 19/87
                c = 66/87
                factor = 9
                return a,b,c,factor
            elif(self.op == 2):
                a = 21/16
                b = 25/16
                c = 19/16
                factor = 17
                return a,b,c,factor

    def generatePossibleSolutions(self, standard_deviation=0.5):
        a, b, c, d = self.solve()

        fake_solutions = 3

        rng = np.random.default_rng()
        s = rng.normal(a, standard_deviation, size=(fake_solutions, 4))
        s = np.append(s, [[a, b, c, d]], axis=0)
        rng.shuffle(s)
        return s