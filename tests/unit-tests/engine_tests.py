import os
import unittest

from application.chess.engine import Engine
from application.chess.chess_game import Chess
from application.chess.fen_operations import Chess

engine_path = '../../chess_engines_cpp/stockfish-10-win/Windows/stockfish_10_x64.exe'

class engine_tests(unittest.TestCase):
    chess=Chess(engine_path)
    chess.start_new_game()
    #engine=Engine()

    def testget_best_moveTest(self): 
        self.chess.start_new_game()
        self.chess.set_fen("r1bqkbnr/pppp1Q1p/2n3p1/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 0 4")
        self.assertEqual(False,self.chess.get_best_move_depth(15),"Function returned false")

    def testset_fen_position(self): 
        self.chess.start_new_game()
        Fen = self.chess.get_fen()
        self.assertEqual("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",Fen,"Fen is wrong")

    def teststart_analyzing_depth(self):
        self.chess.start_new_game()
        evaluationDepth = self.chess.get_evaluation_depth(self)
        self.assertGreaterEqual(1.0,evaluationDepth,"Evaluation is correct")

    def teststart_analyzing_millis(self):
        self.chess.start_new_game()
        evaluationMillis = self.chess.engine.get_evaluation_millis(self)
        self.assertGreaterEqual(1.0,evaluationMillis,"Evaluation is correct")

    #def teststart_analyzing_millis(self):

    #def testget_evaluation_depth():

    #def testget_evaluation_millis():
    def testget_best_move_depth(self):
        self.chess.start_new_game()
        #self.chess.set_fen("r1bqkbnr/pppp1Q1p/2n3p1/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 0 4")
        analyzingDepth = self.chess.engine.get_best_move("r1bqkbnr/pppp1Q1p/2n3p1/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 0 4")
        self.assertNotEqual(True,analyzingDepth,"the best move returns False ")
        

    def testget_best_move_millis(self):
        self.chess.start_new_game()
        analyzingMillis = self.chess.get_best_move_millis(self)
        self.assertNotEqual(True,analyzingMillis,"the best move returns False ")
    #def testget_engine_name():
    

suite = unittest.TestLoader().loadTestsFromTestCase(engine_tests)
unittest.TextTestRunner().run(suite)