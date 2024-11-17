from flask import Blueprint, request, jsonify
import json
import numpy as np

from Utils.JsonUtils import stateToJson
from services import UserService


# Define a Blueprint
home_bp = Blueprint('home', __name__)

@home_bp.route("/register_user", methods=["GET"])
def registerUser():
    user = UserService.registerUser()
    return stateToJson(user)

    #create usr
    #initiate quantum cir
    #give Id

    # ID , state(array d'amplitude) ou objet en format json
@home_bp.route("/get_user", methods=["GET"])
def getUser():
    id = request.args.get("id", 0)
    user = UserService.getUser_from_ID(id)

    return stateToJson(user)


@home_bp.route("/", methods=["GET"])
def home():



    # Call ExampleCircuit if needed
    food_ratings = {"organic dog food": 2, "human food": 10}
    json_format = json.dumps(food_ratings)
    return jsonify(food_ratings)
    #create usr
    #initiate quantum cir
    #give Id

    # ID , state(array d'amplitude) ou objet en format json

