from random import Random

import chess

from application.chess.player import Player


class RandomPlayer(Player):
    def get_best_move(self, fen):
        random = Random()
        board = chess.Board(fen=fen)
        generator = board.legal_moves
        moves = []
        for move in generator:
            moves.append(move)
        return moves[random.randint(0, len(moves) - 1)]
