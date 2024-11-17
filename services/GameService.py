from services.UserService import getUser_from_ID
from services.QuantumCircuitService import quantum_gates

def update_gate(id, gate_type):
    user = getUser_from_ID(id)  # fetch_User
    state = quantum_gates(user.frog_state, gate_type)
    user.setFrogState(state)
    return id, state
