import asyncio
from asyncua import Client, ua
import datetime as dt
import time
import numpy as np
import matplotlib.pyplot as plt
import control as ct
from sympy import *
from scipy import signal

import decimal

zeta = 1/(np.sqrt(2))

# T = the natural period of the system in seconds. Cutoff frequency will be 10 times that.
w0=10*0.63



s = ct.TransferFunction.s

H = 1/((s/(w0))**2+2*zeta*(s/w0) + 1)
print(H)
plt.figure(1)
ct.bode_plot(H, dB=True)



H_discrete = H.sample(0.02)
print(H_discrete)

print(ct.tfdata(H_discrete))
print(H_discrete.zero())
print(H_discrete.pole())