from application.chess.engine import Engine
from application.chess.board_attributes import get_comment

print("Initializing class Engine for module " + __name__ + " ...")
engine = Engine()
print("Engine class initialized successfully!")


def get_strategy_name():
    return "Stockfish"


def get_strategy_move(fen):
    return engine.get_best_move(fen)


def get_strategy_comment(fen, move):
    return get_comment(engine, fen, move)


def get_strategy_short_description():
    return 'Stockfish is consistently ranked first or near the top of most chess-engine rating lists and is the strongest open-source chess engine in the world.'


def get_strategy_description():
    return 'Stockfish is a free and open-source UCI chess engine, available for various desktop and mobile platforms. It is developed by Marco Costalba, Joona Kiiski, Gary Linscott and Tord Romstad, with many contributions from a community of open-source developers. Stockfish is consistently ranked first or near the top of most chess-engine rating lists and is the strongest open-source chess engine in the world. It won the unofficial world computer chess championships in season 6 (2014), season 9 (2016), season 11 (2018), season 12 (2018), and season 13 (2018). It finished runner-up in season 5 (2013), season 7 (2014) and season 8 (2015). As of January 2019, it is the strongest publicly-available chess engine in the world, a fact acknowledged by rival Komodo devloper Larry Kaufman when he said that one must beat Stockfish 10 to claim to be the world\'s best engine. Stockfish is derived from Glaurung, an open-source engine by Romstad.'


def get_strategy_documentation_link():
    return 'https://en.wikipedia.org/wiki/Stockfish_(chess)'
