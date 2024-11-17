from flask import Flask

from controllers.GameController import game_bp
from controllers.UserController import home_bp
from services.UserService import registerUser

app = Flask(__name__)

app.register_blueprint(home_bp)
app.register_blueprint(game_bp)


#hh

if __name__ == '__main__':
    for i in range(4):
        registerUser()

    app.run(debug=True)
