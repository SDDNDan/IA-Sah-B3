import unittest

from application.chess.engine import Engine
from application.chess.chess_game import Chess
from application.chess.fen_operations import Chess
engine_path = '../../chess_engines_cpp/stockfish-10-win/Windows/stockfish_10_x64.exe'
class fen_loaderTester(unittest.TestCase):
    chess=Chess(engine_path)
    chess.start_new_game()
    def get_fens_from_movesTest(self):
        board= set()
        board.add(self.chess.move("e2e4"))
        board.add(self.chess.move("e2e3"))
        self.assertIn(chess.get_fens_from_moves({"e2e4", "e2e3"}),board,"False")
    #def get_fents_from_movesTest():
    #def get_fens_from_pgn_fileTest():
    #def get_fens_from_fen_fileTest():
    #def get_fens_recursivelyTest():

suite = unittest.TestLoader().loadTestsFromTestCase(fen_loaderTester)
unittest.TextTestRunner().run(suite)