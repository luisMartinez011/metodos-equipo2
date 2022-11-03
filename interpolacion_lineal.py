import numpy as np


class interpolacion:

    def __init__(self, a, b, x):
        self.a = a
        self.b = b
        self.x = x
        # a = 2
        # b = 5
        # x = 4

    def solve(self):
        f_a = np.log(self.a)
        f_b = np.log(self.b)

        g_x = (((f_b - f_a) / (self.b-self.a)) * (self.x-self.a)) + f_a
        self.g_x = g_x

        return g_x

    def error(self):
        f_x = np.log(self.x)
        error = abs(f_x - self.g_x)

        return error
