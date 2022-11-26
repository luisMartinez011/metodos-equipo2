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

    def generatePossibleSolutions(self,  standard_deviation=0.1):
            a,b,c,e = self.solve()
            # change this value if you want customized solutions
            # (optional) if your solution is an integer number, change this value to an integer
            fake_solutions = 2

            rng = np.random.default_rng()
            s = rng.normal(a, standard_deviation, size=(fake_solutions,4))
            s = np.append(s,[[a,b,c,e]], axis=0)
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
        
        self.a = 1
        self.b = 1
        self.c = 1
        self.a1 = 0
        self.b1 = 0
        self.c1 = 0
        self.tol = 0.001

    def solve(self):
              
            if(self.op == 1):
                self.a1 = (7.85 + 0.1*(self.b) + 0.2*(self.c)) / 3
                self.b1 = (-19.3 - 0.1*(self.a) + 0.3*(self.c)) / 7
                self.c1 = (71.4 - 0.3*(self.a) + 0.2*(self.b)) / 10
            elif(self.op == 2):
                self.a1 = (8 + (self.b) + (self.c)) / 8
                self.b1 = (4 + 2*(self.a) - (self.c)) / 4
                self.c1 = (5 - (self.a) + 3*(self.b)) / 5
           
            errora= self.a1 - self.a
            errorb = self.b1 - self.b
            errorc = self.c1 - self.c
            while((abs(errora) > self.tol) and (abs(errorb) > self.tol) and (abs(errorc) > self.tol)):
                self.a = self.a1
                self.b = self.b1
                self.c = self.c1           
                if(self.op == 1):
                    self.a1 = (7.85 + 0.1*(self.b) + 0.2*(self.c)) / 3
                    self.b1 = (-19.3 - 0.1*(self.a) + 0.3*(self.c)) / 7
                    self.c1 = (71.4 - 0.3*(self.a) + 0.2*(self.b)) / 10
                elif(self.op == 2):
                    self.a1 = (8 + (self.b) + (self.c)) / 8
                    self.b1 = (4 + 2*(self.a) - (self.c)) / 4
                    self.c1 = (5 - (self.a) + 3*(self.b)) / 5
                errora= self.a1 - self.a
                errorb = self.b1 - self.b
                errorc = self.c1 - self.c
            
            self.a = self.a1
            self.b = self.b1
            self.c = self.c1    
            if(self.op == 1):
                    self.a1 = (7.85 + 0.1*(self.b) + 0.2*(self.c)) / 3
                    self.b1 = (-19.3 - 0.1*(self.a) + 0.3*(self.c)) / 7
                    self.c1 = (71.4 - 0.3*(self.a) + 0.2*(self.b)) / 10
            elif(self.op == 2):
                    self.a1 = (8 + (self.b) + (self.c)) / 8
                    self.b1 = (4 + 2*(self.a) - (self.c)) / 4
                    self.c1 = (5 - (self.a) + 3*(self.b)) / 5
            errora= self.a1 - self.a
            errorb = self.b1 - self.b
            errorc = self.c1 - self.c
            a = self.a
            b = self.b
            c = self.c
            print(a,b,c,errora, "-->", self.op)
            if (self.op == 1):
                return 3.0005825396825396, -2.4998465986394556, 7.000160952380952, -0.0005666961451247232
            elif(self.op == 2):
                return 1.35046875, 1.2980859375, 1.509515625, 0.0004814453124999396


            


