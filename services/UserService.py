from Entities.User import User

user_dict = {}
def registerUser():
    user = User()
    user_dict.update({user.id: user})
    return user

def getUser_from_ID(id):
    return user_dict[id]
