from application.chess.engine import Engine

SPYKE_ENGINE_PATH = '../chess_engines_cpp/Spike/Spike1.4.exe'

print("Initializing class Engine for module " + __name__ + " ...")
engine = Engine(engine_path=SPYKE_ENGINE_PATH)
print("Engine class initialized successfully!")


def get_strategy_name():
    return "Spike"


def get_strategy_move(fen):
    return engine.get_best_move(fen)
