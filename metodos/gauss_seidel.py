from random import randint
import numpy as np

class GaussSeidel :
    
    @staticmethod
    def formula():
        return "/GaussSeidel.png"

    @staticmethod
    def methodName():
        return "Gauss_Seidel"

    def generatePossibleSolutions(self):
        solution, val = self.solve()
        # change this value if you want customized solutions
        # (optional) if your solution is an integer number, change this value to an integer
        standard_deviation = 0.5
        fake_solutions = 4

        rng = np.random.default_rng()
        for r in range(len(val)):
            s = rng.normal(val[r], standard_deviation, fake_solutions)
            r = r + 1
        s = np.append(s, val)
        rng.shuffle(s)
        return s

    def __init__(self):
        selectProblem = randint(1, 2)
        if selectProblem == 1:
            self.A = np.array([[3,-0.1,-0.2],
                               [0.1,7,-0.3],
                               [0.3,-0.2,10]])
            self.B = np.array([[7.85]
                               [-19.3]
                               [71.4]])
            self.problemImage = "GaussSeidel1.png"
        elif selectProblem == 2:
           self.A = np.array([[1,-3,5],
                               [8,-1,-1],
                               [-2,4,1]])
           self.B = np.array([[5]
                               [8]
                               [4]])
           self.problemImage = "GaussSeidel2.png"

        self.X0  = np.array([0.,0.,0.])
        self.tol = 0.001
        self.itermax = 100
        self.tamano = 0.
        self.n = 0
        self.m = 0
        self.X= 0
        self.diferencia = 0
        self.errado = 0

    def solve(self):
        #GaussSeidel
        self.tamano = np.shape(self.A)
        self.n = self.tamano[0]
        self.m = self.tamano[1]
        #Valores iniciales
        self.X = np.copy(self.X0)
        self.diferencia = np.ones(self.n, dtype=float)
        self.errado = 2*self.tol

        k = 0
        while not (self.errado <= self.tol or k > self.itermax):
            #Por fila
            for i in range(0,self.n,1):
                suma = 0
                #Por columna
                for j in range(0,self.m,1):
                    #Excluir diagonal A
                    if(i != j):
                        suma = suma + self.A[i,j] * self.X[j]
                    
                nuevo = (self.B[i] + suma) / self.A[i,i]
                self.diferencia[i] = np.abs(nuevo-self.X[i])
                self.X[i] = nuevo
            self.errado = np.max(self.diferencia)
            k += 1
        #Respuesta de X en columna
        self.X = np.transpose([self.X])
        if(k>self.itermax):
            self.X = 0
        self.verificar = np.dot(self.A,self.X)
        x = self.X
        alter = self.verificar

        return x , alter
    def error(self):
        alter = self.verificar
        return alter        

