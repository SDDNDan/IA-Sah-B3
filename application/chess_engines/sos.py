from application.chess.engine import Engine


def get_strategy_name():
    return "SOS"


def get_strategy_move(fen):
    engine = Engine(engine_path='../chess_engines_cpp/SOS/SOS-51_Arena.exe')
    return engine.get_best_move(fen)
