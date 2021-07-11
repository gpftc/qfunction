from qfunction.bloch_sphere import animate_bloch
from qfunction.tri import q_cos,q_sin
from qutip import *
import numpy as np

q = 1.8
states = []
thetas = np.linspace(0,2*np.pi,20)
for theta in thetas:
    states.append((q_cos(theta/2,q=q)*basis(2,0) + q_sin(theta/2,q=q)*basis(2,1)).unit())
print(states)
animate_bloch(states, duration=0.1, save_all=False)
