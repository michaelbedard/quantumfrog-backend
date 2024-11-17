from qiskit.quantum_info import Statevector

from Entities.User import User

user_dict = {}
def registerUser():
    user = User()
    user_dict.update({user.id: user})
    return user


def get_user_from_id(id):
    try:
        # Ensure id is an integer
        id = int(id)
    except ValueError:
        # Handle case where id cannot be converted to an integer
        return None

    return user_dict.get(id)

def getUser_from_ID(id):
    try:
        # Ensure id is an integer
        id = int(id)
    except ValueError:
        # Handle case where id cannot be converted to an integer
        return None

    return user_dict.get(id)





