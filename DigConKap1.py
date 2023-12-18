import control as ct
import matplotlib.pyplot as plt
import math
from sympy import *
import scipy.signal

s = ct.TransferFunction.s

H = 5/(10*s+1)
Z = ct.tf([1],[1,-0.67],0.1)
Z = Z * ct.tf([1,-1],[1,0],0.1)
print(H)

G_discrete = H.sample(1)
print(H)
print()
print(G_discrete)

t,y=ct.step_response(H)
t1,y1=ct.step_response(G_discrete)
plt.figure(1)
plt.plot(t,y)
plt.figure(2)
plt.plot(t1,y1)

plt.show()