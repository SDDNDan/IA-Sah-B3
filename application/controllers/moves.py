from common_lib.package_operations import package_contents
from common_lib.fen_operations import valid_fen
import importlib
import json

CHESS_ENGINES_PACKAGE = 'chess_engines'


def get_moves_controller(request):
    fen = request.args.get('fen', type=str)
    strategy = request.args.get('strategy', default='all', type=str).lower()

    if not valid_fen(fen):
        return 'Fen is missing or is invalid!', 400

    answer = []
    for chess_engine in package_contents(CHESS_ENGINES_PACKAGE):
        if (strategy == 'all' or strategy == chess_engine) and chess_engine != '__init__':
            chess_engine_module = importlib.import_module(
                ".".join([CHESS_ENGINES_PACKAGE, chess_engine]))

            answer.append({"strategy": chess_engine_module.get_strategy_name(
            ), "move": chess_engine_module.get_strategy_move(fen)})

    if len(answer) == 0:
        return 'Strategy with name \'{}\' is not recognized!'.format(strategy), 400

    return json.dumps(answer)
