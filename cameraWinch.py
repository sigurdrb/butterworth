from scipy import signal
from scipy import optimize
from scipy.signal import cont2discrete, lti, dlti, dstep
import numpy as np
import control as ct
import matplotlib.pyplot as plt



def enc_to_pos(L1,L2,D,F,k):
    
    theta1 = np.arcsin((L1**2+D**2-L2**2)/(2*L1*D))
    theta2 = np.arcsin((L2**2+D**2-L1**2)/(2*L2*D))

    T_1 = F/(np.sin(theta1)+np.cos(theta1)*np.tan(theta2))
    T_2 = (T_1*np.cos(theta1))/(np.cos(theta2))

    dL1 = k * T_1
    dL2 = k * T_2



    for i in range(100):
        L1 = L1+dL1
        L2 = L2+dL2

        theta1 = np.arcsin((L1**2+D**2-L2**2)/(2*L1*D))
        theta2 = np.arcsin((L2**2+D**2-L1**2)/(2*L2*D))

        T_1 = F/(np.sin(theta1)+np.cos(theta1)*np.tan(theta2))
        T_2 = (T_1*np.cos(theta1))/(np.cos(theta2))

        dL1 = k * T_1 
        dL2 = k * T_2 

        print(theta1)
    return dL1


enc_to_pos(11,16,20,3,0.02)