from qfunction.quantum import QuantumCircuit as Qc
from qfunction.quantum import simulator as sim
from qfunction.plot import plot_probabilities as pp


q = 0.1
qc = Qc(5,q=q)

print(qc.q_qubits)
qc.Y(2)
qc.H(2)


print(qc)
pp(qc)
print(sim(qc))
#pp(qc)
#for q in 