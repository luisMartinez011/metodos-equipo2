from random import randint
import numpy as np
from metodos.metodos_padre import Metodo_Padre


class GaussJordan(Metodo_Padre):

    @staticmethod
    def formula():
        return "/Gauss.jpg"

    @staticmethod
    def methodName():
        return "Gauss_Jordan"

    def __init__(self):
        selectProblem = randint(1, 2)
        selectProblem = 2
        if selectProblem == 1:
            self.A = np.array([[4, 2, 5],
                               [2, 5, 8],
                               [5, 4, 3]])
            self.B = np.array([[60.70],
                               [92.90],
                               [56.30]])
            self.problemImage = "Gauss1.png"
        elif selectProblem == 2:
            self.A = np.array([[3, -2, 2],
                               [4, 2, 2],
                               [3, -3, 3]])
            self.B = np.array([[1],
                               [2],
                               [3]])
            self.problemImage = "Gauss2.png"
        self.casicero = 1e-15
        self.AB = 0
        self.AB0 = 0
        self.n = 0
        self.m = 0
        self.tamaño = 0
        self.columna = 0
        self.dondemax = 0
        self.pivote = 0
        self.adelante = 0
        self.atras = 0
        self.factor = 0
        self.x = 0
        self.AB1 = 0

        def generatePossibleSolutions(self):
            a,b,c,fact = self.solve()
            # change this value if you want customized solutions
            # (optional) if your solution is an integer number, change this value to an integer
            standard_deviation = 0.5
            fake_solutions = 3

            rng = np.random.default_rng()
            s = rng.normal(a, standard_deviation, size=(fake_solutions,4))
            s = np.append(s,[[a,b,c,fact]], axis=0)
            rng.shuffle(s)
            return s

    def solve(self):
        self.A = np.array(self.A, dtype=float)
        # Matriz aumentada
        self.AB = np.concatenate((self.A, self.B), axis=1)
        self.AB0 = np.copy(self.AB)
        # pivoteo por filas
        self.tamaño = np.shape(self.AB)
        self.n = self.tamaño[0]
        self.m = self.tamaño[1]
        # Para cada fila en AB
        for i in range(0, self.n-1, 1):
            # columna desde diagonal
            self.columna = abs(self.AB[i:, i])
            self.dondemax = np.argmax(self.columna)
            # donde max no es diagonal
            if (self.dondemax != 0):
                temporal = np.copy(self.AB[i, :])
                self.AB[i, :] = self.AB[self.dondemax+i, :]
                self.AB[self.dondemax+i, :] = temporal
        self.AB1 = np.copy(self.AB0)
        ultfila = self.n-1
        ultcolumna = self.m-1
        # Eliminaciones
        for i in range(0, self.n-1, 1):
            self.pivote = self.AB[i, i]
            self.adelante = i + 1
            for k in range(self.adelante, self.n, 1):
                self.factor = self.AB[k, i]/self.pivote
                self.AB[k, :] = self.AB[k, :] - self.AB[i, :]*self.factor
            self.AB[i, :] = self.AB[i, :] / self.AB[i, i]
        self.x = np.copy(self.AB[:, ultcolumna])
        self.x = np.transpose([self.x])
        a = self.x[0]
        b = self.x[1]
        c = self.x[2]
        fact = self.factor
        return a,b,c,fact

    def error(self):
        i = 3
        pivotex = []
        for fila in self.AB1:
            pivotex.append(fila[i])
        pivotex = np.transpose(pivotex)
        return pivotex
