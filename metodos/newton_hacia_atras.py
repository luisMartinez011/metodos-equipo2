import pandas as pd
import numpy as np
import functools


class Newton_hacia_atras:

    def __init__(self):
        self.x = 3
        xi = [1.7, 2.4, 3.1]
        yi = [0.35, 0.87, 1.03]

        self.coords = pd.DataFrame(list(zip(xi, yi)),
                                   columns=["xi", "yi"])

    @staticmethod
    def formula():
        return "Newton_hacia_atras.png"

    # returns the method name
    @staticmethod
    def methodName():
        return "Newton hacia atras"

    def solve(self):
        roundValue = 9
        save_H_Values = []

        for i in range(len(self.coords.xi)):
            if i == 0:
                continue
            save_H_Values.append(
                np.round(self.coords.xi[i] - self.coords.xi[i-1], roundValue))

        is_H_Unique = save_H_Values.count(
            save_H_Values[0]) == len(save_H_Values)
        if (is_H_Unique):
            h = save_H_Values[0]
        else:
            print("No tiene intervalos uniformes h")

        s = np.round((self.x - self.coords.xi[2]) / h, roundValue)

        s0 = 1
        s1 = s
        s2 = s*(s+1) / np.math.factorial(2)

        delta = []

        def agregarDelta(x, y):
            delta.append(np.round((y-x), roundValue))
            return y

        for i in range(len(self.coords.yi)-1):
            if i == 0:
                functools.reduce(agregarDelta, self.coords.yi)
            else:
                savePreviousDeltas = list(delta)
                functools.reduce(agregarDelta, savePreviousDeltas)

        g_x = self.coords.yi[2] * s0 + delta[1]*s1 + delta[2] * s2
        g_x = np.round(g_x, roundValue)
        return g_x
