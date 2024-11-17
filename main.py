from flask import Flask
from flask_cors import CORS


from controllers.GameController import game_bp
from controllers.UserController import home_bp
from services.UserService import registerUser

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://localhost:3000", "https://quantumfrog-frontend-je6u9m75w-michael-bedards-projects.vercel.app/"]}})

app.register_blueprint(home_bp)
app.register_blueprint(game_bp)


#hh

if __name__ == '__main__':
    for i in range(4):
        registerUser()

    app.run(debug=True)
