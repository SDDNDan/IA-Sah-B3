from application.common_lib.package_operations import list_package_modules
import importlib
import chess
import json
import re

CHESS_ENGINES_PACKAGE_NAME = 'application.chess_engines'
game_checker_re = re.compile("([a-h][1-8][a-h][1-8]){4,}$")


def get_commentary_controller(request):
    print('Starting to generate new commentary ...')
    game = request.args.get('game', type=str).lower()

    if game is None or not game_checker_re.match(game):
        return 'Game sequence is invalid or missing!', 400

    moves = [game[pos:pos+4] for pos in range(0, len(game), 4)]
    current_board = chess.Board()
    answer = []

    for move in moves:
        answer.append([])

        for chess_engine_module_name in list_package_modules(CHESS_ENGINES_PACKAGE_NAME):
            chess_engine_module = importlib.import_module(
                chess_engine_module_name)

            if chess_engine_module.get_strategy_name() != "Stockfish":
                continue

            try:
                commentary, strategy_best_move = chess_engine_module.get_strategy_comment(
                    current_board.fen(), move)
                if commentary is not None:
                    answer[-1].append(
                        {"strategy": chess_engine_module.get_strategy_name(), "commentary": commentary, "fen": current_board.fen(), "userMove": move, "suggestedMove": strategy_best_move})
            except ValueError as e:
                print("Error generating commentaries: {}".format(e))
                return 'Invalid move {} after {} moves!'.format(move, len(answer) - 1), 400

        current_board.push_uci(move)

    return json.dumps(answer)
