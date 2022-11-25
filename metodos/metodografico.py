import numpy as np
import random


class Grafico:

    def generatePossibleSolutions(self, standard_deviation=0.1):
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
        return "Metodo_Grafico"

    def __init__(self):

        self.x = np.array([ -3,-2, -1, 0, 1, 2, 3])
        self.y = np.array([ 0, 0, 0])
        self.problemImage = "grafico1.png"

    def funcion(self,x):
        yf = pow(x,3) - 6.5*x + 2
        return yf
    def solve(self):
        i = 0
        k= 0
        ant = 1
        post = -1
        for i in range(len(self.x)-1):
            a = self.x[i]
            b = self.x[i+1]
            ant = pow(a,3) - 6.5*a + 2
            post =pow(b,3) - 6.5*b + 2
            if(ant > 0 and post < 0):
                self.y[k] = ant
                k = k + 1
            elif(ant < 0 and post > 0):
                self.y[k] = post
                k = k + 1
                
        y1 = self.y[0]
        y2 = self.y[1]
        y3 = self.y[2]
        return y1, y2, y3

        
