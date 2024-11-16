import numpy as np
from numpy.linalg import norm

class StateDescriptor:
    def __set__(self, instance, value):
        print(f"Setting value: {value}")
        instance._value = value

    def __get__(self, instance, owner):
        return instance._value

class MyClass:
    attribute = MyDescriptor()

# Normal usage via instance
obj = MyClass()
obj.attribute = 42  # Triggers MyDescriptor.__set__

print(obj.attribute


def __set__(self, instance, state: Union[list, np.ndarray]):
    if (round(norm(state)) != 1):
        raise ValueError("The state should be normalized to one")
    if (len(state) != 2):
        raise Exception("The state should only contain two amplitude values")
    if type(state) == list:
        state = np.ndarray(state)
    print(f"Setting state: {state}")
    instance._state = state

    return state

