from qfunction.quantum.equations import S,S_q
from qfunction.fundamentals import q_cos,q_sin
from numpy import array,linspace,pi

t = array([1,2,34,56,34,23])
p = t/t.sum()
#print(p)
#print(S(p))

t = linspace(-2,2,100)*2*pi

theta = t/2
gamma = t
q =1
print(S_q(theta,gamma,q))

q = .5
print(S_q(theta,gamma,q))

q = 1.5
print(S_q(theta,gamma,q))