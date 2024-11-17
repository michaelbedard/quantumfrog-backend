import numpy as np
from Descriptors.StateDescriptor import StateDescriptor
from qiskit.quantum_info import Statevector
from services.WorldService import get_default_world, get_firefly_world
from services.IdService import getNextId

class User(object):
    id: int
    frog_state: Statevector
    firefly_state : Statevector

    def __init__(self):
        self.id = getNextId()
        self.frog_state = get_default_world()
        self.firefly_state = get_firefly_world()

    def setFrogState(self, state:Statevector):
        self.frog_state = state



