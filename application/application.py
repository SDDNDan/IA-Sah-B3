from flask import Flask
from flask import request
from flask_cors import CORS

from controllers.moves import get_moves_controller

app = Flask(__name__)
CORS(app)


@app.route('/moves', methods=['GET'])
def get_moves_router():
    return get_moves_controller(request)
