from application.chess.random_player import RandomPlayer


def get_strategy_name():
    return "Random"


def get_strategy_move(fen):
    rand_player = RandomPlayer()
    return rand_player.get_best_move(fen)
