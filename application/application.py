from flask import Flask
from flask import request
from flask_cors import CORS

from application.controllers.moves import get_moves_controller
from application.controllers.strategies import get_strategies_controller

app = Flask(__name__)
CORS(app)


@app.route('/moves', methods=['GET'])
def get_moves_router():
    return get_moves_controller(request)


@app.route('/strategies', methods=['GET'])
def get_strategies_router():
    return get_strategies_controller(request)
