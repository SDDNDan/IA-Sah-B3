from application.chess.engine import Engine


def get_strategy_name():
    return "Rybka"


def get_strategy_move(fen):
    engine = Engine(engine_path='../chess_engines_cpp/Rybka/Rybkav2.3.2a.mp.x64.exe')
    return engine.get_best_move(fen)