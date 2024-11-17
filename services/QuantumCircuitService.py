import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector


# Proximity index : how close are the firefly and frog states
def get_proximity_index(firefly, frog):

    # inner product
    inner_product = firefly.inner(frog)

    # proximity index from 0 to 1: 0 -> orthogonal states; 1 -> identical states
    # (ignoring the global phase factor)
    # It's the probability that the 2 states would be aligned if measured
    proximity_index = abs(inner_product) ** 2
    return proximity_index

# Quantum transformations
def quantum_gates(state, gate):

    if not isinstance(state, Statevector):
        raise ValueError("TypeError : state has to be a Statevector.")

    # Validity of the gate
    valid_gates = ['h', 'x', 'z', 'r']
    if gate not in valid_gates:
        raise ValueError(f"The gate'{gate}' is invalid. Please use 'h', 'x', 'z' or 'r'.")

    # Creating one qubit circuit
    qc = QuantumCircuit(1)

    # Apply specified state
    # Hadamard
    if gate == 'h':
        qc.h(0)
    # Bit flip
    elif gate == 'x':
        qc.x(0)
    # Phase flip
    elif gate == 'z':
        qc.z(0)
    # pi/4 rotation (anticlockwise)
    elif gate == 'r':
        qc.ry(np.pi / 4, 0)

    # Apply the circuit to the initial state using Statevector.evolve.
    final_state = state.evolve(qc)

    return final_state






