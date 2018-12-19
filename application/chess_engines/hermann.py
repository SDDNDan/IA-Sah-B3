from application.chess.engine import Engine

HERMANN_ENGINE_PATH = '../chess_engines_cpp/Hermann/Hermann28_64.exe'

print("Initializing class Engine for module " + __name__ + " ...")
engine = Engine(engine_path=HERMANN_ENGINE_PATH)
print("Engine class initialized successfully!")


def get_strategy_name():
    return "Hermann"


def get_strategy_move(fen):
    return engine.get_best_move(fen)
