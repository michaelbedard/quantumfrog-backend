
import numpy as np
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator
from qiskit import QuantumCircuit, transpile


def get_proximity_index(firefly, frog):
    # inner product
    inner_product = firefly.inner(frog)

    # proximity index from 0 to 1: 0 -> orthogonal states; 1 -> identical states (ignoring the global phase factor)
    # It's the probability that the 2 states would be aligned if measured
    proximity_index = abs(inner_product) ** 2
    return proximity_index

def gates(state, gate):

    # making sure state is a Statevector
    if not isinstance(state, Statevector):
        raise ValueError("Type error : should be a Statevector")

    valid_gates = ['h', 'x', 'z']
    if gate not in valid_gates:
        raise ValueError(f"The gate '{gate}' is invalid. Please enter either h, x or z.")

    # Define quantum circuit
    qc = QuantumCircuit(1)

    if gate == 'h':
        qc.h(0)
    elif gate == 'z':
        qc.z(0)
    elif gate == 'x':
        qc.x(0)


    # Use AerSimulator directly
    simulator = AerSimulator()
    qc.save_statevector()

    # Compile and run the circuit on the simulator
    transpiled_qc = transpile(qc, simulator)
    result = simulator.run(transpiled_qc, initial_state=state).result()

    # Get the final statevector
    final_state = result.get_statevector()

    return final_state



state = Statevector([0,1])
print(gates(state, 'h'))
print(gates(state, 'x'))
print(gates(state, 'z'))

state2 = Statevector([1, 0])

print(get_proximity_index(state, state2))
