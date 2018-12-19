from application.chess.engine import Engine

ANMON_ENGINE_PATH = '../chess_engines_cpp/AnMon/AnMon_5.75.exe'

print("Initializing class Engine for module " + __name__ + " ...")
engine = Engine(engine_path=ANMON_ENGINE_PATH)
print("Engine class initialized successfully!")


def get_strategy_name():
    return "AnMon"


def get_strategy_move(fen):
    return engine.get_best_move(fen)
