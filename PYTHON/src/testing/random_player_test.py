from random import Random

from PYTHON.src.chess.chess_game import Chess
from PYTHON.src.chess.engine import Engine
from PYTHON.src.chess.random_player import RandomPlayer

game_count = 2000
sf_wins = 0
for i in range(game_count):
    print("Playing game: " + str(i))
    chess = Chess()
    random = Random()
    is_sf_white = bool(random.getrandbits(1))
    if is_sf_white:
        white = Engine()
        black = RandomPlayer()
    else:
        white = RandomPlayer()
        black = Engine()
    while not chess.is_over():
        white_move = white.get_best_move(chess.get_fen())
        chess.move(white_move)
        if not chess.is_over():
            black_move = black.get_best_move(chess.get_fen())
            chess.move(black_move)
    if is_sf_white == chess.is_white_winner():
        sf_wins += 1
print(sf_wins)
