import numpy as np
import random


class Grafico:

    def generatePossibleSolutions(self, standard_deviation=1):
        a,b,c = self.solve()

        fake_solutions = 4

        rng = np.random.default_rng()
        s = rng.normal(a, standard_deviation, size=(fake_solutions,3))
        s = np.append(s, [[a,b,c]], axis=0)
        rng.shuffle(s)
        return s

    @staticmethod
    def formula():
        return "/graficoa.png"

    @staticmethod
    def methodName():
        return "Método_Grafico"

    def __init__(self):
        selectProblem = random.randint(1, 2)
        if selectProblem == 1:
            self.x = np.array([ -3,-2, -1, 0, 1, 2, 3])
            self.y = np.array([ 0, 0, 0])
            self.problemImage = "grafico1.png"
            self.op = 1
        elif selectProblem == 2:
            self.x = np.array([ -3,-2, -1, 0, 1, 2, 3])
            self.y = np.array([ 0, 0, 0])
            self.problemImage = "grafico2.png"
            self.op = 2

    def solve(self):
        i = 0
        k= 0
        ant = 1
        post = -1
        for i in range(len(self.x)-1):
            a = self.x[i]
            b = self.x[i+1]

            if self.op == 1:
                ant = pow(a,3) - 6.5*a + 2
                post =pow(b,3) - 6.5*b + 2
            else:
                ant = (2 * pow(a,2)) - (6 * a) - 3
                post= (2 * pow(b,2)) - (6 * b) - 3

            if(ant > 0 and post < 0):
                self.y[k] = ant
                if k != 3:
                    k = k + 1
            elif(ant < 0 and post > 0):
                self.y[k] = post
                if k != 3:
                    k = k + 1

        y1 = self.y[0]
        y2 = self.y[1]
        y3 = self.y[2]
        return y1, y2, y3


