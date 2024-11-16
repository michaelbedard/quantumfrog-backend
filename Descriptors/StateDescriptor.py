import numpy as np
from numpy.linalg import norm
from typing import Union


class StateDescriptor:
    def __init__(self, state: Union[list, np.ndarray]):
        self.typeVerify(self)
        self.state = state

    def __set__(self, instance, state: Union[list, np.ndarray]):
        self.typeVerify(self, instance, state)
        instance._value = state

    def __get__(self, instance, owner):
        return instance._value

    def typeVerify(self, state):
        if (round(norm(state)) != 1):
            raise ValueError("The state should be normalized to one")
        if (len(state) != 2):
            raise Exception("The state should only contain two amplitude values")
        if type(state) == list:
            self.state = np.array(state)
