from application.chess.engine import Engine


def get_strategy_name():
    return "Stockfish"


def get_strategy_move(fen):
    engine = Engine()
    return engine.get_best_move(fen)
