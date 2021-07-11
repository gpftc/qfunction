from qfunction.quantum import QuantumCircuit as Qc
from qfunction.quantum.algorithms import ArenaGame

q = .9
qc = Qc(1,q=q)
game = ArenaGame(qc=qc)

game.up()
game.left()
game.left()
game.show()