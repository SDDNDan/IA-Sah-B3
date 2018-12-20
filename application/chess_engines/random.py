from application.chess.random_player import RandomPlayer
from application.chess.board_attributes import get_comment


def get_strategy_name():
    return "Random"


def get_strategy_move(fen):
    rand_player = RandomPlayer()
    return str(rand_player.get_best_move(fen))
