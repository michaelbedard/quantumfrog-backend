from qiskit import QuantumCircuit
import numpy as np
from qiskit.quantum_info import Statevector
import random

def rotated_state(theta):
    a = np.cos(theta)
    b = np.sin(theta)
    return [a, b]


worlds = {
    "|0>": Statevector([1, 0]),
    "|1>": Statevector([0, 1]),
    "|+>": Statevector([1 / np.sqrt(2), 1 / np.sqrt(2)]),
    "|->": Statevector([1 / np.sqrt(2), -1 / np.sqrt(2)]),
    "|22.5>": Statevector(rotated_state(np.deg2rad(22.5))),
    "|72.5>": Statevector(rotated_state(np.deg2rad(72.5))),
    "|-22.5>": Statevector(rotated_state(np.deg2rad(-22.5))),
    "|-72.5>": Statevector(rotated_state(np.deg2rad(-72.5))),

}

# Randomly chose worlds for the firefly and the frog
available_keys = [key for key in worlds.keys() if key != "|0>"]
firefly_key = random.choice(available_keys)
firefly = worlds[firefly_key]

frog = worlds["|0>"]

print(frog.data, firefly.data, frog)

# inner product
inner_product = firefly.inner(frog)

# proximity index from 0 to 1: 0 -> orthogonal states; 1 -> identical states (ignoring the global phase factor)
# It's the probability that the 2 states would be aligned if measured
proximity_index = abs(inner_product) ** 2

print(proximity_index)



