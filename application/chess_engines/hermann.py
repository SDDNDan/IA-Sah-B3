from application.chess.engine import Engine


def get_strategy_name():
    return "Hermann"


def get_strategy_move(fen):
    engine = Engine(engine_path='../chess_engines_cpp/Hermann/Hermann28_32.exe')
    #engine = Engine(engine_path='../chess_engines_cpp/Hermann/Hermann28_64.exe')
    return engine.get_best_move(fen)
