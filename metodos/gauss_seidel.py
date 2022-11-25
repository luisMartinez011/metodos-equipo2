from random import randint
import numpy as np
from metodos.metodos_padre import Metodo_Padre


class GaussSeidel:

    @staticmethod
    def formula():
        return "/GaussSeidel.png"

    @staticmethod
    def methodName():
        return "Gauss_Seidel"

    def generatePossibleSolutions(self):
        a,b,c = self.solve()
        # change this value if you want customized solutions
        # (optional) if your solution is an integer number, change this value to an integer
        standard_deviation = 0.5
        fake_solutions = 3

        rng = np.random.default_rng()
        s = rng.normal(a, standard_deviation, size=(fake_solutions,3))
        s = np.append(s, [[a,b,c]], axis=0)
        rng.shuffle(s)
        return s

    def generatePossibleSolutions(self, standard_deviation=0.5):
            a,b,c = self.solve()
            # change this value if you want customized solutions
            # (optional) if your solution is an integer number, change this value to an integer
            fake_solutions = 2

            rng = np.random.default_rng()
            s = rng.normal(a, standard_deviation, size=(fake_solutions,3))
            s = np.append(s,[[a,b,c]], axis=0)
            rng.shuffle(s)
            return s

    def __init__(self):

        selectProblem = randint(1, 2)
        if selectProblem == 1:
            self.A = np.array([[3, -0.1, -0.2],
                            [0.1, 7, -0.3],
                            [0.3, -0.2, 10]])
            self.B = np.array([[7.85],
                            [-19.3],
                            [71.4]])
            self.problemImage = "jacobi1.png"
            self.op = 1
        elif selectProblem == 2:
            self.A = np.array([[3, -0.1, -0.2],
                            [0.1, 7, -0.3],
                            [0.3, -0.2, 10]])
            self.B = np.array([[7.85],
                            [-19.3],
                            [71.4]])
            self.problemImage = "jacobi2.png"
            self.op = 2

        self.a = 0
        self.b = 0
        self.c = 0
        self.a1 = 0
        self.b1 = 0
        self.c1 = 0
        self.tol = 0.001

    def solve(self):

            auxa = self.a
            auxb = self.b
            auxc = self.c
            if(self.op == 1):
                self.a1 = (7.85 + 0.1*(self.b) + 0.2*(self.c)) / 3
                self.a = self.a1
                self.b1 = (-19.3 - 0.1*(self.a) + 0.3*(self.c)) / 7
                self.b = self.b1
                self.c1 = (71.4 - 0.3*(self.a) + 0.2*(self.b)) / 10
                self.c = self.c1
            elif(self.op == 2):
                self.a1 = (8 + (self.b) + (self.c)) / 8
                self.a = self.a1
                self.b1 = (4 + 2*(self.a) - (self.c)) / 4
                self.b = self.b1
                self.c1 = (5 - (self.a) + 3*(self.b)) / 5
                self.c = self.c1

            errora= self.a1 - auxa
            errorb = self.b1 - auxb
            errorc = self.c1 - auxc
            while((abs(errora) > self.tol) and (abs(errorb) > self.tol) and (abs(errorc) > self.tol)):
                auxa = self.a
                auxb = self.b
                auxc = self.c
                if(self.op == 1):
                    self.a1 = (7.85 + 0.1*(self.b) + 0.2*(self.c)) / 3
                    self.a = self.a1
                    self.b1 = (-19.3 - 0.1*(self.a) + 0.3*(self.c)) / 7
                    self.b = self.b1
                    self.c1 = (71.4 - 0.3*(self.a) + 0.2*(self.b)) / 10
                    self.c = self.c1
                elif(self.op == 2):
                    self.a1 = (8 + (self.b) + (self.c)) / 8
                    self.a = self.a1
                    self.b1 = (4 + 2*(self.a) - (self.c)) / 4
                    self.b = self.b1
                    self.c1 = (5 - (self.a) + 3*(self.b)) / 5
                    self.c = self.c1
                errora= self.a1 - auxa
                errorb = self.b1 - auxb
                errorc = self.c1 - auxc

                auxa = self.a
                auxb = self.b
                auxc = self.c
            if(self.op == 1):
                self.a1 = (7.85 + 0.1*(self.b) + 0.2*(self.c)) / 3
                self.a = self.a1
                self.b1 = (-19.3 - 0.1*(self.a) + 0.3*(self.c)) / 7
                self.b = self.b1
                self.c1 = (71.4 - 0.3*(self.a) + 0.2*(self.b)) / 10
                self.c = self.c1
            elif(self.op == 2):
                self.a1 = (8 + (self.b) + (self.c)) / 8
                self.a = self.a1
                self.b1 = (4 + 2*(self.a) - (self.c)) / 4
                self.b = self.b1
                self.c1 = (5 - (self.a) + 3*(self.b)) / 5
                self.c = self.c1
            errora= self.a1 - auxa
            errorb = self.b1 - auxb
            errorc = self.c1 - auxc
            a = self.a
            b = self.b
            c = self.c
            return a,b,c
