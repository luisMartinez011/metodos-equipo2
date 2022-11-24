import numpy as np
import random


class Grafico:

    def generatePossibleSolutions(self, standard_deviation=0.5):
        a,b,c = self.solve()

        fake_solutions = 3

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
        return "Metodo_Grafico"

    def __init__(self):
        self.x = [[-3],[-2],[-1],[0],[1],[2],[3]]
        self.y = ([0],[0],[0])
        self.problemImage = "grafico1.png"
    def funcion(self,x):
        yf = pow(x,3) - 6.5*x + 2
        return yf
    def solve(self):
        i = 0
        ant = 1
        post = -1
        for i in range(len(self.x)-1):
            ant = self.funcion(self.x[i])
            post = self.funcion(self.x[i+1])
            if(ant > 0 and post < 0):
                self.y[i] = ant
            elif(ant < 0 and post > 0):
                self.y[i] = post
        y1 = self.y[0]
        y2 = self.y[1]
        y3 = self.y[2]
        print(self.y)
        return y1, y2, y3

        
