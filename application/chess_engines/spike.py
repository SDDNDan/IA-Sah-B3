from application.chess.engine import Engine
from application.chess.board_attributes import get_comment

SPYKE_ENGINE_PATH = '../chess_engines_cpp/Spike/Spike1.4.exe'

print("Initializing class Engine for module " + __name__ + " ...")
engine = Engine(engine_path=SPYKE_ENGINE_PATH)
print("Engine class initialized successfully!")


def get_strategy_name():
    return "Spike"


def get_strategy_move(fen):
    return engine.get_best_move(fen)


def get_strategy_comment(fen, move):
    return get_comment(engine, fen, move)


def get_strategy_short_description():
    return 'Spike is a chess engine developed since spring 2004. It is developed from the scratch but uses many ideas already tested on our two other engines: Cheetah and IceSpell.'


def get_strategy_description():
    return 'Spike is a typically brute force program with a pvs algorithm. The board structure is a kind of 0x88 but has an additional border above and below the chesseld. The board has 14x16 elds to make move generation as easy as possible. With the version 1.0 Spike got some new pruning rules, the biggest prunings are Nullmove (for a long time already), History (Version 1.0) and Futility (Version 1.1). The eval checks pawn structure (double, isolated, backward, passed, connected and combinations of them), king security, pawn shield, mobility, piece attack/defence, rook on open lines, rook or queen on 7-th or 8-th row, knight and bishop position, trapped rooks and knights outposts supported by own pawns that cannot be attacked by opponents pawns.'


def get_strategy_documentation_link():
    return 'http://spike.lazypics.de/index_en.html'
