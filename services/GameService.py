from services.UserService import getUser_from_ID, registerUser
from services.QuantumCircuitService import quantum_gates
from qiskit.quantum_info import Statevector

def update_gate(id, gate_type):
    user = getUser_from_ID(id)  # fetch_User
    state = quantum_gates(user.frog_state, gate_type)
    user.setFrogState(state)
    return id, state
def get_bracket(id):
    user = getUser_from_ID(id)
    user.frog_state.draw(output='latex')

mike = registerUser()
get_bracket(1)



