from application.chess.engine import Engine

SOS_ENGINE_PATH = '../chess_engines_cpp/SOS/SOS-51_Arena.exe'

print("Initializing class Engine for module " + __name__ + " ...")
engine = Engine(engine_path=SOS_ENGINE_PATH)
print("Engine class initialized successfully!")


def get_strategy_name():
    return "SOS"


def get_strategy_move(fen):
    return engine.get_best_move(fen)
