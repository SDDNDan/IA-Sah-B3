from application.chess.engine import Engine
from application.chess.board_attributes import get_comment

RUFFIAN_ENGINE_PATH = '../chess_engines_cpp/Ruffian/Ruffian_105.exe'

print("Initializing class Engine for module " + __name__ + " ...")
engine = Engine(engine_path=RUFFIAN_ENGINE_PATH)
print("Engine class initialized successfully!")


def get_strategy_name():
    return "Ruffian"


def get_strategy_move(fen):
    return engine.get_best_move(fen)


def get_strategy_comment(fen, move):
    return get_comment(engine, fen, move)
