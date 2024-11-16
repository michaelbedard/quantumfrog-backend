from flask import Blueprint, request, jsonify
import json

from services import UserService
from json import JSONEncoder
from Entities.JSON import NumpyArrayEncoder

# Define a Blueprint
home_bp = Blueprint('home', __name__)

@home_bp.route("/register_user", methods=["GET","POST"])
def registerUser():
    user = UserService.registerUser()

    numpyData = {"id": user.id, "state": user.state.data.real}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)

    return jsonify(encodedNumpyData)

    #create usr
    #initiate quantum cir
    #give Id

    # ID , state(array d'amplitude) ou objet en format json

@home_bp.route("/", methods=["GET"])
def getUser():
    id = request.args.get("id", 0)


    # Call ExampleCircuit if needed
    food_ratings = {"organic dog food": 2, "human food": 10}
    json_format = json.dumps(food_ratings)
    return jsonify(food_ratings)
    #create usr
    #initiate quantum cir
    #give Id

    # ID , state(array d'amplitude) ou objet en format json

