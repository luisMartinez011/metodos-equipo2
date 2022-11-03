import numpy as np

a = 2
b = 5
x = 4

f_a = np.log(a)
f_b = np.log(b)

g_x = (((f_b - f_a) / (b-a)) * (x-a)) + f_a
g_x
f_x = np.log(x)

error = abs(f_x - g_x)
