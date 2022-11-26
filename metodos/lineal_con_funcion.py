import numpy as np
from random import randint
from metodos.metodos_padre import Metodo_Padre


class Lineal_con_funcion:

    def __init__(self):
        selectProblem = randint(1, 2)
        self.x = np.array([1.1, 1.9, 2.4, 4.8, 5.1, 10.5])
        self.y = np.array([2.5, 2.7, 3.7, 5.2, 6.0, 8.3])
        self.fx = np.sin(np.deg2rad(self.x))
        self.problemImage = "Lineal_con_funcion_1.png"

    @staticmethod
    def formula():
        return "Lineal_con_funcion.png"

    @staticmethod
    def methodName():
        return "Lineal con funcion"

    def solve(self):
        x = self.x
        y = self.y
        fx = self.fx
        n = len(x)
        sum_x = sum(x)
        sum_squared_x = sum(i*i for i in x)
        sum_fx_and_x = sum(a*b for a,b in zip(x,fx))

        sum_y = sum(y)
        sum_squared_y = sum(i*i for i in x)
        sum_fx_and_y = sum(a*b for a,b in zip(y,fx))

        sum_xy = sum(a * b for a,b in zip(x,y))

        sum_fx = sum(fx)
        sum_squared_fx = sum(i*i for i in fx)

        a = np.array([[n,sum_x,sum_fx],[sum_x,sum_squared_x,sum_fx_and_x],
                    [sum_fx,sum_fx_and_x, sum_squared_fx]])
        b = np.array([sum_y,sum_xy, sum_fx_and_y])

        first, second,third = np.linalg.solve(a,b)
        return first, second,third

    # override this method to generate two anwsers per option
    def generatePossibleSolutions(self, standard_deviation=0.5):
        a, b, c = self.solve()

        fake_solutions = 3

        rng = np.random.default_rng()
        s = rng.normal(a, standard_deviation, size=(fake_solutions, 3))
        s = np.append(s, [[a, b, c]], axis=0)
        rng.shuffle(s)
        return s
