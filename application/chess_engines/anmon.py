from application.chess.engine import Engine


def get_strategy_name():
    return "AnMon"


def get_strategy_move(fen):
    engine = Engine(engine_path='../chess_engines_cpp/AnMon/AnMon_5.75.exe')
    return engine.get_best_move(fen)