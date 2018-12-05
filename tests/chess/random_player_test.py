from random import Random

from application.chess.chess_game import Chess
from application.chess.engine import Engine
from application.chess.random_player import RandomPlayer

game_count = 20
sf_wins = 0
sf = Engine()
rand_player = RandomPlayer()
chess = Chess()

for i in range(game_count):
    print("Playing game: " + str(i))
    chess.start_new_game()
    random = Random()
    is_sf_white = bool(random.getrandbits(1))
    if is_sf_white:
        white = sf
        black = rand_player
    else:
        white = rand_player
        black = sf
    while not chess.is_over():
        white_move = white.get_best_move(chess.get_fen())
        chess.move(white_move)
        if not chess.is_over():
            black_move = black.get_best_move(chess.get_fen())
            chess.move(black_move)
    if is_sf_white == chess.is_white_winner():
        sf_wins += 1
print("Stockfish wins: " + str(sf_wins))
