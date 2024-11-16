
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

def get_firefly_world():
    available_keys = [key for key in worlds.keys() if key != "|0>"]
    firefly_key = random.choice(available_keys)
    firefly = worlds[firefly_key]
    return firefly

def get_default_world():
    return worlds["|0>"]




