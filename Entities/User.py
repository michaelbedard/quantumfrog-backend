import numpy as np
from Descriptors.StateDescriptor import StateDescriptor
from qiskit.quantum_info import Statevector
from services.WorldService import get_default_world


class User(object):
    id_counter = 0

    def __init__(self):
        self.id = User.id_counter
        User.id_counter += 1
        self.state = get_default_world()


    def setState(self, state):
        self.state = state
