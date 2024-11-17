import numpy as np
from qiskit.quantum_info import Statevector

from services.UserService import getUser_from_ID, registerUser
from services.QuantumCircuitService import quantum_gates
from flask_cors import CORS

from services.WorldService import rotated_state


def update_gate(id, gate_type):
    user = getUser_from_ID(id)  # fetch_User
    state = quantum_gates(user.frog_state, gate_type)
    user.setFrogState(state)
    return id, state
def get_bracket(id):
    user = getUser_from_ID(id)
    bracket = user.frog_state.draw(output='latex_source')
    return bracket

worlds = {
    "0.3826834324 |0\\rangle-0.9238795325 |1\\rangle": 0,
    "\\frac{\\sqrt{2}}{2} |0\\rangle- \\frac{\\sqrt{2}}{2} |1\\rangle": 1,
    "0.9238795325 |0\\rangle-0.3826834324 |1\\rangle": 2,
    " |0\\rangle": 3,
    "0.9238795325 |0\\rangle+0.3826834324 |1\\rangle": 4,
    "\\frac{\\sqrt{2}}{2} |0\\rangle+\\frac{\\sqrt{2}}{2} |1\\rangle": 5,
    "0.3826834324 |0\\rangle+0.9238795325 |1\\rangle": 6,
    " |1\\rangle": 7

}
"""
worlds = {
    "0.3826834324 |0\\rangle-0.9238795325 |1\\rangle": "|-67.5>",
    "\\frac{\\sqrt{2}}{2} |0\\rangle- \\frac{\\sqrt{2}}{2} |1\\rangle": "|->",
    "0.9238795325 |0\\rangle-0.3826834324 |1\\rangle": "|-22.5>",
    " |0\\rangle": "0",
    "0.9238795325 |0\\rangle+0.3826834324 |1\\rangle": "|22.5>",
    "\\frac{\\sqrt{2}}{2} |0\\rangle+\\frac{\\sqrt{2}}{2} |1\\rangle": "|+>",
    "0.3826834324 |0\\rangle+0.9238795325 |1\\rangle": "|67.5>",
    " |1\\rangle": "|1>"

}
"""
def get_world_id(string):
    world_id = worlds[string]
#mike = registerUser()
#text = get_bracket(1)
#print(text)



