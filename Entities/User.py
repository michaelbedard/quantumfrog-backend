from typing import Union

import numpy as np
from numpy.linalg import norm


class User:
    id_counter = 0
    def __init__(self):
        self.id = User.id_counter
        User.id_counter += 1
        self.state = np.array([0,0])



mike = User()
mike.state = [0,1]
print(mike.state)
print(type(mike.state))


