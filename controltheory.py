import control as ct
import matplotlib.pyplot as plt


s = ct.TransferFunction.s
tau=0.16
P=5+0.3*s+5/(s*tau)
G=1/(0.01*s**2+0.11*s+0.1)
H=P*G/(1+P*G)
print(ct.poles(H))
fig, ax = plt.subplots(figsize=(15,8))



ax.set_xlabel('Real', fontsize=14)
ax.set_ylabel('Imaginary', fontsize=14)

ax.tick_params(axis='both', labelsize=14)
roots, gains = ct.root_locus(H,plot=True, print_gain=True,ax=ax)
fig.savefig('root_locus.png',dpi=600)



t,y=ct.step_response(G)
plt.figure(2)
plt.plot(t,y)


plt.show()