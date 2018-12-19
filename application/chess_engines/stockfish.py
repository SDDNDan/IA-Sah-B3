from application.chess.engine import Engine
from application.chess.board_attributes import get_comment


def get_strategy_name():
    return "Stockfish"


def get_strategy_move(fen):
    engine = Engine()
    return engine.get_best_move(fen)


def get_strategy_comment(fen, move):
    engine = Engine()
    return get_comment(engine, fen, move)
