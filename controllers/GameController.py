from flask import Blueprint, request, jsonify

from Utils.JsonUtils import stateToJson
from Utils.latexUtils import parse_latex_to_string
from services import UserService
from services.QuantumCircuitService import quantum_gates
from services.GameService import update_gate, get_bracket, get_world_id
from services.QuantumCircuitService import get_proximity_index
from services.UserService import getUser_from_ID
# Define a Blueprint
game_bp = Blueprint('game', __name__)


@game_bp.route("/traverse_gate", methods=["GET"])
def gate():
    id = request.args.get("id", 0)
    gate_type = request.args.get("gate", 'i')
    (id, state) = update_gate(id, gate_type)

    user = UserService.getUser_from_ID(id)

    return stateToJson(user)

@game_bp.route("/get_probability", methods=["GET"])
def getProb():
    id = request.args.get("id", 0)
    user = getUser_from_ID(id)
    prox_index = get_proximity_index(user.frog_state, user.firefly_state)

    return jsonify(prox_index)

@game_bp.route("/get_bracket", methods=["GET"])
def getBracket():
    id = request.args.get("id", 0)
    latex_source = get_bracket(id)
    id = get_world_id(str(latex_source))
    return jsonify(id)

@game_bp.route("/get_world", methods=["GET"])
def getWorld():
    id = request.args.get("id", 0)
    user = getUser_from_ID(id)
    world = getWorld(user.frog_state)
    return jsonify(world)


