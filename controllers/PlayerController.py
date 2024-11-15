from flask import Blueprint

# Define a Blueprint
home_bp = Blueprint('home', __name__)

@home_bp.route("/")
def home():
    # Call ExampleCircuit if needed
    return "Test"
