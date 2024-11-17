from flask import Flask
from flask_cors import CORS

from controllers.GameController import game_bp
from controllers.UserController import home_bp
from services.UserService import registerUser

app = Flask(__name__)

CORS(app, supports_credentials=True, origins=[
    "http://localhost:3000",
    "https://quantumfrog-frontend.vercel.app",
    "https://quantumfrog-frontend-pduuzbfv6-michael-bedards-projects.vercel.app",
    "https://quantumfrog-frontend-git-main-michael-bedards-projects.vercel.app",
    "https://quantumfrog-frontend-je6u9m75w-michael-bedards-projects.vercel.app"
])

app.register_blueprint(home_bp)
app.register_blueprint(game_bp)

if __name__ == '__main__':
    for i in range(4):
        registerUser()

    app.run(debug=True)

##huuh

@app.after_request
def add_dynamic_origin(response):
    origin = request.headers.get('Origin')
    if origin in [
        "http://localhost:3000",
        "https://quantumfrog-frontend.vercel.app",
        "https://quantumfrog-frontend-pduuzbfv6-michael-bedards-projects.vercel.app",
        "https://quantumfrog-frontend-git-main-michael-bedards-projects.vercel.app",
        "https://quantumfrog-frontend-je6u9m75w-michael-bedards-projects.vercel.app"
    ]:
        response.headers['Access-Control-Allow-Origin'] = origin
    return response

# @app.after_request
# def add_cors_headers(response):
#     response.headers["Access-Control-Allow-Origin"] = "*"
#     response.headers["Access-Control-Allow-Credentials"] = "true"
#     response.headers["Access-Control-Allow-Headers"] = "Content-Type,Authorization"
#     response.headers["Access-Control-Allow-Methods"] = "GET,POST,OPTIONS"
#     return response
