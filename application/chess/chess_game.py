import chess

from application.chess.engine import Engine


class Chess:

    def __init__(self, engine_path=None, engine_name=None):
        self.engine_path = engine_path
        if engine_path is None:
            self.stockfish = Engine()
        else:
            self.stockfish = Engine(engine_path)
        self.board = chess.Board()
        self.engine_name = engine_name

    def start_new_game(self):
        self.board = chess.Board()
        self.stockfish.set_fen_position(self.board.fen())

    def undo_last_move(self):
        self.board.pop()
        self.stockfish.set_fen_position(self.board.fen())

    def move(self, move_uci):
        self.board.push_uci(str(move_uci))
        self.stockfish.set_fen_position(self.board.fen())

    def get_best_move_depth(self, depth):
        return self.stockfish.get_best_move_depth(depth)

    def get_best_move_millis(self, millis):
        return self.stockfish.get_best_move_millis(millis)

    def get_best_move_from_fen_millis(self, fen, millis):
        sf = Engine(self.engine_path)
        sf.set_fen_position(fen)
        return sf.get_best_move_millis(millis)

    def get_best_move_from_fen_depth(self, fen, depth):
        sf = Engine(self.engine_path)
        sf.set_fen_position(fen)
        return sf.get_best_move_depth(depth)

    def get_fen(self):
        return self.board.fen()

    def get_evaluation_depth(self, depth):
        if not self.is_white_to_move():
            sign = -1
        else:
            sign = 1
        return sign * self.stockfish.get_evaluation_depth(depth)

    def is_white_to_move(self):
        return self.board.fen().split(" ")[-5] == "w"

    def get_valid_moves(self):
        return self.board.legal_moves

    def is_over(self):
        return self.board.is_game_over()

    def is_white_winner(self):
        return not self.is_white_to_move() and self.board.is_checkmate()

    def set_fen(self, fen):
        self.board.set_fen(fen)
        self.stockfish.set_fen_position(fen)
