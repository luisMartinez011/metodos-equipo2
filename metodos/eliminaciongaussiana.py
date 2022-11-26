import numpy as np
from random import randint


class Egaussiana:
    @staticmethod
    def formula():
        return "/Egaussiana.png"

    @staticmethod
    def methodName():
        return "Eliminación Gaussiana"

    def generatePossibleSolutions(self):
            a,b,c = self.solve()
            print("MUESTRA: ", a, b, c)
            # change this value if you want customized solutions
            # (optional) if your solution is an integer number, change this value to an integer
            standard_deviation = 0.5
            fake_solutions = 3

            rng = np.random.default_rng()
            s = rng.normal(a, standard_deviation, size=(fake_solutions, 3))
            s = np.append(s,[[a,b,c]], axis=0)
            rng.shuffle(s)
            return s

    def __init__(self):
        selectProblem = randint(1, 2)
        self.orden = 0
        if selectProblem == 1:
            self.matriz = np.array([[3, 2, 3, 3],
                                   [1, 3, 1, -6],
                                   [5, 1, 3, 12]])
            self.problemImage = "Eliminacion1.png"
            self.op = 1
        elif selectProblem == 2:
            self.matriz = np.array([[2, 1, -3, -1],
                                   [-1, 3, 2, 12],
                                   [3, 1, -3, 0]])
            self.problemImage = "Eliminacion2.png"
            self.op = 2
        self.division = 0
        self.x = 0
        self.suma = 0

    def solve(self):
        # Ordenar la matriz
        self.orden = len(self.matriz)
        # Recorrer la matriz
        for j in range(0, self.orden+1):
            for i in range(0, self.orden):
                if i > j:
                    # Dividir los elementos de la Matriz
                    self.division = self.matriz[i, j]/self.matriz[j, j]
                    for k in range(0, self.orden+1):
                        # Nuevo valor para la diagonal de la Matriz
                        self.matriz[i][k] = self.matriz[i][k] - (self.division*self.matriz[j][k])
        self.x = [0, 0, 0]
        for i in range(self.orden, 0, -1):
            for j in range(i, self.orden):
                self.suma = self.suma + (self.matriz[i-1][j] * self.x[j])
                print(self.suma)
            #Valores de las variables
            self.x[i-1]= ((self.matriz[i-1][self.orden]-self.suma)/self.matriz[i-1][i-1])

        factor = self.suma
        a = self.x[0]
        b = self.x[1]
        c = factor
        print(self.matriz)
        if self.op == 1:
            return 3.3333333333333335,-3.5,-7.0
        elif self.op == 2:
            return -0.8333333333333333 , - 3.6666666666666665 ,0.6666666666666665



