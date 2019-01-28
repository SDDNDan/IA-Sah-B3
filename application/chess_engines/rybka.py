from application.chess.engine import Engine
from application.chess.board_attributes import get_comment

RYBKA_ENGINE_PATH = '../chess_engines_cpp/Rybka/Rybkav2.3.2a.mp.x64.exe'

print("Initializing class Engine for module " + __name__ + " ...")
engine = Engine(engine_path=RYBKA_ENGINE_PATH)
print("Engine class initialized successfully!")


def get_strategy_name():
    return "Rybka"


def get_strategy_move(fen):
    return engine.get_best_move(fen)


def get_strategy_comment(fen, move):
    return get_comment(engine, fen, move)


def get_strategy_short_description():
    return 'Rybka is a chess engine designed by Vasik Rajlich, an International Master. Rybka was one of the top-rated engines on chess engine rating lists and has won many computer chess tournaments.'


def get_strategy_description():
    return 'Rybka is a chess engine designed by Vasik Rajlich, International Master. Rybka was one of the top-rated engines on chess engine rating lists and has won many computer chess tournaments and it uses a bitboard representation and is an alpha-beta searcher (search algorithm that seeks to decrease the number of nodes that are evaluated by the minimax algorithm in its search tree). It uses very aggressive pruning, leading to imbalanced search trees. The details of the evaluation function of this engine are unknown.'


def get_strategy_documentation_link():
    return 'https://en.wikipedia.org/wiki/Rybka'
