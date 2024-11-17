from flask import Blueprint, request, jsonify

from Utils.JsonUtils import toJson
from services import UserService
from services.QuantumCircuitService import quantum_gates
from services.GameService import update_gate

# Define a Blueprint
game_bp = Blueprint('game', __name__)


@game_bp.route("/traverse_gate", methods=["GET", "POST"])
def gate():
    id = request.args.get("id", 0)
    gate_type = request.args.get("gate", 'i')
    (id, state) = update_gate(id, gate_type)

    user = UserService.getUser_from_ID(id)

    return toJson(user)

@game_bp.route("/get_probability", methods=["GET", "POST"])
def getProb():

    return "not yet"
