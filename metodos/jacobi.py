from random import randint
import numpy as np
from metodos.metodos_padre import Metodo_Padre


class Jacobi:
    @staticmethod
    def formula():
        return "jacobi.png"

    @staticmethod
    def methodName():
        return "Jacobi"

    def generatePossibleSolutions(self):
            a,b,c,fact = self.solve()
            # change this value if you want customized solutions
            # (optional) if your solution is an integer number, change this value to an integer
            standard_deviation = 0.5
            fake_solutions = 3

            rng = np.random.default_rng()
            s = rng.normal(s, standard_deviation, size=(fake_solutions,4))
            s = np.append(s,[[a,b,c,fact]], axis=0)
            rng.shuffle(s)
            return s

    def __init__(self):
        selectProblem = randint(1, 2)
        self.A = np.array([[3, -0.1, -0.2],
                           [0.1, 7, -0.3],
                           [0.3, -0.2, 10]])
        self.B = np.array([[7.85],
                           [-19.3],
                           [71.4]])
        self.problemImage = "jacobi1.png"
        self.x0 = 0
        self.x1 = 0
        self.tol = 0.001

    def solve(self):
                self.x0 = np.zeros(4)
                self.x1 = np.zeros(4)
                while abs(self.x1 - self.x0) < self.tol :
                    self.x0 = self.x1
                    self.x1[0] = (self.B[0] - self.A[0,1] * self.x0[1] - self.A[0,2] * self.x0[2] - self.A[0,3] * self.x0[3]) / self.A[0,0]
                    self.x1[1] = (self.B[1] - self.A[1,0] * self.x0[0] - self.A[1,2] * self.x0[2] - self.A[1,3] * self.x0[3]) / self.A[1,1]
                    self.x1[2] = (self.B[2] - self.A[2,0] * self.x0[0] - self.A[2,1] * self.x0[1] - self.A[2,3] * self.x0[3]) / self.A[2,2]
                    self.x1[3] = (self.B[3] - self.A[3,0] * self.x0[0] - self.A[3,1] * self.x0[1] - self.A[3,2] * self.x0[2]) / self.A[3,3]
                    k = k + 1
                error = abs(self.x1 - self.x0)
                a = self.x1[0] #numeros de la ecuacion
                b = self.x1[1]
                c = self.x1[2]
                return a,b,c,error
