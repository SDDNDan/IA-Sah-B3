import chess

from application.chess.engine import Engine


class Chess:

    def __init__(self, engine_path=None, engine_name=None):
        self.engine_path = engine_path
        if engine_path is None:
            self.engine = Engine()
        else:
            self.engine = Engine(engine_path)
        self.board = chess.Board()
        self.engine_name = engine_name

    def start_new_game(self):
        self.board = chess.Board()
        self.sync_engine()

    def undo_last_move(self):
        self.board.pop()
        self.sync_engine()

    def move(self, move_uci):
        self.board.push_uci(str(move_uci))
        self.sync_engine()

    def get_best_move_depth(self, depth):
        return self.engine.get_best_move_depth(depth)

    def get_best_move_millis(self, millis):
        return self.engine.get_best_move_millis(millis)

    def get_best_move_from_fen_millis(self, fen, millis):
        self.engine.set_fen_position(fen)
        move = self.engine.get_best_move_millis(millis)
        self.sync_engine()
        return move

    def get_best_move_from_fen_depth(self, fen, depth):
        self.engine.set_fen_position(fen)
        move = self.engine.get_best_move_depth(depth)
        self.sync_engine()
        return move

    def get_fen(self):
        return self.board.fen()

    def get_evaluation_depth(self, depth):
        if not self.is_white_to_move():
            sign = -1
        else:
            sign = 1
        return sign * self.engine.get_evaluation_depth(depth)

    def is_white_to_move(self):
        return self.board.fen().split(" ")[-5] == "w"

    def get_valid_moves(self):
        moves_str = []
        moves = self.board.legal_moves
        for move in moves:
            moves_str.append(move.uci())
        return moves_str

    def is_over(self):
        return self.board.is_game_over()

    def is_white_winner(self):
        return not self.is_white_to_move() and self.board.is_checkmate()

    def set_fen(self, fen):
        self.board.set_fen(fen)
        self.sync_engine()

    def sync_engine(self):
        self.engine.set_fen_position(self.board.fen())
