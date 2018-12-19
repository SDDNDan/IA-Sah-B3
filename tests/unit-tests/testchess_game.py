import unittest

from application.chess.engine import Engine
from application.chess.chess_game import Chess
engine_path = '../../chess_engines_cpp/stockfish-10-win/Windows/stockfish_10_x64.exe'
class testchess_game(unittest.TestCase):
    chess=Chess(engine_path)
    chess.start_new_game()
    def testGetfen(self):
        boardFen=self.chess.get_fen()
        self.assertEqual("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",boardFen,"Fen getter is wrong")
   
    def testMoveTest(self):
        self.chess.move("e2e4")
        boardFen=self.chess.get_fen()
        self.assertEqual("rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1",boardFen, "Moving didn't work corectly")
        
    def testundo_last_move(self):
        self.chess.start_new_game()
        self.chess.move("e2e4")
        self.chess.undo_last_move()
        boardFen=self.chess.get_fen()
        self.assertEqual("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",boardFen,"Undo is not working")
    
    def testis_white_to_moveTest(self):
        self.chess.start_new_game()
        self.assertEqual(True,self.chess.is_white_to_move(),"It's black turn to move")

    def testis_overTest(self):
        self.chess.set_fen("r1bqkbnr/pppp1Q1p/2n3p1/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 0 4")
        self.assertEqual(True,self.chess.is_over(), "Function returned false")
    
    def testis_white_winnerTest(self):
        self.chess.set_fen("r1bqkbnr/pppp1Q1p/2n3p1/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 0 4")
        self.assertEqual(True,self.chess.is_white_winner(), "Function returned false")
    

suite = unittest.TestLoader().loadTestsFromTestCase(testchess_game)
unittest.TextTestRunner().run(suite)
    
