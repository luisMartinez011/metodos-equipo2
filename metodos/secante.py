import pandas as pd
import numpy as np
import functools
from mpmath import *

class Secante():

    def __init__(self):
        self.x1 = 1 # valor siguiente del intervalo
        self.x0 = 0 # valor anterior del intervalo (se sustituye por el valor de x1)
        self.fx1 = 0
        self.fx0 = 0
        self.x= 0
    @staticmethod
    def formula():
        return "Secante.png"

    @staticmethod
    def methodName():
        return "Secante"

    #Funciones para calcular x0 y x1 
    def funx0(self):
        self.fx0 = round(exp(-self.x0) - self.x0, 9)
    def funx1(self):
         self.fx1 = round(exp(-self.x1) - self.x1 , 9)
    #Funcion general para x
    def funx(self):
        x = round(self.x1 - ((self.fx1 * (self.x1 - self.x0)) / (self.fx1 - self.fx0)) , 9)
        return x
    #Calculo del error

    def solve(self):
        self.funx0()
        while abs(self.x1 - self.x0) > 0.001 :
            self.funx1()
            nx = self.funx()
            self.x0 = self.x1
            self.fx0 = self.fx1
            self.x1 = nx
        #Imprime el resultado buscar la manera de imprirlo en la interfaz
        print("{:.9f}".format(self.x1) , " ----" , "{:.9f}".format(abs(self.x1 - self.x0)))
    def error(self):
        err = abs(self.x1 - self.x0)
        return err
test = Secante()
test.solve()