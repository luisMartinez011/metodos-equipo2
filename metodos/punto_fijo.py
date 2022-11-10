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
        self.coords = pd.DataFrame(list(zip(aux, m)),
                                   columns=["Indice A", "Indice B", "Margen Error"])
        print(df);
        while(abs(a-m)>tol):
            a=m;
            aux=m;
            m=f(a);
            print('El intervalo es [', aux, ',' , m , ']');
            k = k+1;

        print('x',k,'=',m,'es la mejor aproximacion');
        print ('Aproximacion = ' , (a-m) , ', Margen error: ', tol);

  


    

