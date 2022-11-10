import pandas as pd
import numpy as np
import functools
from math import *


class PuntoFijo:
    tol = 10**(-5)
    a=0;
    @staticmethod
    def formula():
        return "Ayuda_PuntoFijo.png"

    @staticmethod
    def methodName():
        return "Punto Fijo"
    def f(x):
        return exp(-x)
    def solve(self):
        aux=0;
        m=f(a);
        k=0;
        iA =[]
        while(abs(a-m)>tol):
            a=m;
            aux=m;
            m=f(a);

            k = k+1;
            iA.append[aux];
            iB.append[m];
            iE.append[(a-m)];
            
       self.coords = pd.DataFrame(list(zip(iA, iB, iE)),
                                   columns=["Indice A", "Indice B", "Margen Error"])
    def error(self):
        e = self.a - self.m;
        return abs(e);

  


    

