import numpy as np
import sympy as sp
import functools
from random import randint
from math import *

def f(t,y):
    func=t*exp(3*t)-2*y
    return func 

def eulermod(t,y,h,n):
    print('y(',t,')=',y)
    for k in range(n):
        y0=y+h*f(t,y)
        y=y+(h/2)*(f(t,y)+f(t+h,y0))
        t=t+h
        print('y(',t,')=',y)
        
eulermod(0,1.2,0.3,2)