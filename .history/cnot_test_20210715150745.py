from qfunction.quantum import QuantumCircuit as Qc
from qfunction.plot.histogram import plot_cnot_prob as pcp

q =1.1
qc = Qc(4,q=q)
print(qc.cnot((2,1)))
print(qc)