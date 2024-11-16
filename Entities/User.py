import numpy as np
from Descriptors.StateDescriptor import StateDescriptor


class User(object):
    id_counter = 0

    def __init__(self, state):
        self.id = User.id_counter
        User.id_counter += 1
        self.state = StateDescriptor(state)

mike = User([0,1])
#mike.state = [0,1]
print(mike.state)
print(type(mike.state))

class State:
