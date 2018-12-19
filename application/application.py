from flask import Flask
from flask import request
from flask_cors import CORS
from application.controllers.strategies import get_strategies_controller
from application.controllers.moves import get_moves_controller
from application.controllers.commentary import get_commentary_controller

app = Flask(__name__)
CORS(app)


@app.route('/strategies', methods=['GET'])
def get_strategies_router():
    return get_strategies_controller(request)


@app.route('/moves', methods=['GET'])
def get_moves_router():
    return get_moves_controller(request)


@app.route('/commentary', methods=['GET'])
def get_commentary_router():
    return get_commentary_controller(request)
