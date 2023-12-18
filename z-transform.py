import control as ct
import matplotlib.pyplot as plt
import math
from sympy import *
import scipy.signal

s = ct.TransferFunction.s

H = 1/(4*s)
print(H)

H_discrete = H.sample(1)
print(H_discrete)

t,y=ct.step_response(H)
t1,y1=ct.step_response(H_discrete)
plt.figure(1)
plt.plot(t,y)
plt.figure(2)
plt.plot(t1,y1)
plt.show()

