from application.chess.engine import Engine
from application.chess.board_attributes import get_comment

print("Initializing class Engine for module " + __name__ + " ...")
engine = Engine()
print("Engine class initialized successfully!")


def get_strategy_name():
    return "Stockfish"


def get_strategy_move(fen):
    return engine.get_best_move(fen)


def get_strategy_comment(fen, move):
    return get_comment(engine, fen, move)
