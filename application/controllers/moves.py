from application.common_lib.package_operations import list_package_modules
from application.chess.fen_operations import valid_fen
import importlib
import json
import time

CHESS_ENGINES_PACKAGE_NAME = 'application.chess_engines'


def current_millis_time(): return int(round(time.time() * 1000))


def get_moves_controller(request):
    fen = request.args.get('fen', type=str)
    strategy = request.args.get('strategy', default='all', type=str).lower()

    if not valid_fen(fen):
        return 'Fen is missing or is invalid!', 400

    start_millis_controller = current_millis_time()
    answer = []
    for chess_engine_module_name in list_package_modules(CHESS_ENGINES_PACKAGE_NAME):
        if (strategy == 'all' or strategy == chess_engine_module_name.split(".")[-1]):
            chess_engine_module = importlib.import_module(
                chess_engine_module_name)

            starting_millis_strategy = current_millis_time()
            print("Trying to get answer from {} ...".format(
                chess_engine_module.get_strategy_name()))
            answer.append({"strategy": chess_engine_module.get_strategy_name(
            ), "move": chess_engine_module.get_strategy_move(fen)})
            finish_millis_strategy = current_millis_time()
            print("Successfully got answer from {} in {}ms!".format(
                chess_engine_module.get_strategy_name(), finish_millis_strategy - starting_millis_strategy))
    finish_millis_controller = current_millis_time()
    print("Total time to get answer: {}ms!".format(
        finish_millis_controller - start_millis_controller))

    if len(answer) == 0:
        return 'Strategy with name \'{}\' is not recognized!'.format(strategy), 400

    return json.dumps(answer)
