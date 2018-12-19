from application.common_lib.package_operations import list_package_modules
from application.chess.fen_operations import valid_fen
import importlib
import json

CHESS_ENGINES_PACKAGE_NAME = 'application.chess_engines'


def get_moves_controller(request):
    fen = request.args.get('fen', type=str)
    strategy = request.args.get('strategy', default='all', type=str).lower()

    if not valid_fen(fen):
        return 'Fen is missing or is invalid!', 400

    answer = []
    for chess_engine_module_name in list_package_modules(CHESS_ENGINES_PACKAGE_NAME):
        if (strategy == 'all' or strategy == chess_engine_module_name.split(".")[-1]):
            chess_engine_module = importlib.import_module(chess_engine_module_name)

            answer.append({"strategy": chess_engine_module.get_strategy_name(
            ), "move": chess_engine_module.get_strategy_move(fen)})

    if len(answer) == 0:
        return 'Strategy with name \'{}\' is not recognized!'.format(strategy), 400

    return json.dumps(answer)
