import control as ct
import matplotlib.pyplot as plt
import math
from sympy import *
import scipy.signal
import time

mk = 1
yk1 = 0
i = 1
y=[]

while i < 100:
    yk = 0.5*mk-0.1*yk1
    yk1 = yk
    y.append(yk)
    i = i +1

print(y)
plt.figure(1)
plt.plot(y)
plt.show()