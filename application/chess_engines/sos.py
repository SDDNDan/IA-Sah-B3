from application.chess.engine import Engine
from application.chess.board_attributes import get_comment

SOS_ENGINE_PATH = '../chess_engines_cpp/SOS/SOS-51_Arena.exe'

print("Initializing class Engine for module " + __name__ + " ...")
engine = Engine(engine_path=SOS_ENGINE_PATH)
print("Engine class initialized successfully!")


def get_strategy_name():
    return "SOS"


def get_strategy_move(fen):
    return engine.get_best_move(fen)


def get_strategy_comment(fen, move):
    return get_comment(engine, fen, move)


def get_strategy_short_description():
    return 'SOS is a chess engine developed and written by Rudolf Huber which has been developing since 1990s.'


def get_strategy_description():
    return 'SOS uses depth first minimax tree search with quiescence search, alpha-beta enhancement, minimal window search and null-move pruning. To improve the search efficiency, the history heuristic and a trans-positional table is used. The evaluation parameters are dynamic and continuously updated during tree search. SOS\'s weakest part is probably endgame knowledge. SOS actively plays a wide Chess Mentor Backend Technical Report 9 range of openings, but most of those lines are not very deep. With auto-play games against itself, the opening book is tuned to favor those lines which harmonize with SOS\'s style of play'


def get_strategy_documentation_link():
    return 'http://www.playwitharena.com/?Partner_Chess_Engines:SOS%26nbsp%3B'
