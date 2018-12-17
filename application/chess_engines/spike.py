from application.chess.engine import Engine


def get_strategy_name():
    return "Spike"


def get_strategy_move(fen):
    engine = Engine(engine_path='../chess_engines_cpp/Spike/Spike1.4.exe')
    return engine.get_best_move(fen)
