from flask import Flask
from controllers.PlayerController import home_bp

app = Flask(__name__)

app.register_blueprint(home_bp)

#hh

if __name__ == '__main__':
    app.run(debug=True)
