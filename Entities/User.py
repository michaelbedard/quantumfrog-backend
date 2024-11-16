import numpy as np
from Descriptors.StateDescriptor import StateDescriptor


class User(object):
    id_counter = 0

    def __init__(self):
        self.id = User.id_counter
        User.id_counter += 1
        self.state = StateDescriptor()

mike = User()
mike.state = [0,1]
print(mike.state)
print(type(mike.state))
