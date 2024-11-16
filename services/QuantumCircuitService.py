
import numpy as np
from qiskit.quantum_info import Statevector
from qiskit import QuantumCircuit, Aer, transpile


def get_proximity_index(firefly, frog):
    # inner product
    inner_product = firefly.inner(frog)

    # proximity index from 0 to 1: 0 -> orthogonal states; 1 -> identical states (ignoring the global phase factor)
    # It's the probability that the 2 states would be aligned if measured
    proximity_index = abs(inner_product) ** 2
    return proximity_index

def hadamard_gate(state):
    # making sure state is a Statevector
    if not isinstance(state, Statevector):
        raise ValueError("Type error : should be a Statevector")

    qc = QuantumCircuit(1)
    qc.h(0)

    # Quantum state simulator
    backend = Aer.get_backend('statevector_simulator')

    # Compute circuit
    qc.save_statevector()
    result = backend.run(transpile(qc, backend), initial_state=state).result()

    final_state = result.get_statevector()

    return final_state




