from qiskit import QuantumCircuit


def ExampleCircuit():
    qc = QuantumCircuit(1, 1)
    qc.h(0)

    print("Quantum Circuit:")
    print(qc)
