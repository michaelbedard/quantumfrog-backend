from flask import Blueprint, request, jsonify

from Utils.JsonUtils import toJson
from services import UserService
from services.QuantumCircuitService import quantum_gates
from controllers.UserController import home_bp
from services.GameService import update_gate


@home_bp.route("/traverse_gate", methods=["GET", "POST"])
def gate(id, gate_type):
    id = request.args.get("id", 0)
    (id, state) = update_gate(id, gate_type)

    user = UserService.getUser_from_ID(id)

    return toJson(user)

@home_bp.route("\get_probability", methods=["GET", "POST"])
def getProb():

    return "not yet"
