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


def get_strategy_short_description():
    return 'Ruffian is a strong chess engine which has been developing since 1998.'


def get_strategy_description():
    return 'Ruffian is a strong chess engine that can be loaded as a winboard or UCI engine. Ruffian supports most winboard (version 1 and 2) and UCI options. The program has been developing in C language since 1998. It has used various known techniques like bitboards (combines it with 8x8 representation), null move, prunning, extensions. The opening library is not of high quality and sophisticated, it was automatically generated from a small PGN database.'


def get_strategy_documentation_link():
    return 'http://www.top-5000.nl/int/ruffian.htm'
