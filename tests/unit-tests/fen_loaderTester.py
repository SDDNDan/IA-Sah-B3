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

    def test_validFen(self):
        move=self.chess.set_fen("r1bqkbnr/pppp1Q1p/2n3p1/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 0 4")
        self.assertEqual(valid_fen(move),True)

    def test_invalidFen(self):
        move=self.chess.set_fen("r1bqkbnr/pppp1Q1p/2n3p1/4p3/2B1P3/8/PPQP1PPP/RNB1Q1NR b KQkq - 0 4")
        self.assertEqual(valid_fen(move),False)

suite = unittest.TestLoader().loadTestsFromTestCase(fen_loaderTester)
unittest.TextTestRunner().run(suite)