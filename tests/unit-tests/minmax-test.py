import unittest

from application.chess.engine import Engine
from application.chess.chess_game import Chess
from application.chess_engines import minmax

engine_path = '../../chess_engines/minmax.py'


class minmax_test(unittest.TestCase):
    chess = Chess(engine_path)
    chess.start_new_game()

    fen = "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1"

    minmax_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

    minmax_expected_fen = "r1bqkbnr/pppp1Q1p/2n3p1/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 0 4"

    def test_posible_test_should_return_empty(self, fen=fen):
        states = minmax.get_possible_states(fen)
        self.assertEqual(states, [])

    def test_posible_test_(self, fen=minmax_fen):
        states = minmax.get_possible_states(fen)
        self.assertTrue(len(states) != 0)

    def test_get_name(self):
        self.assertEqual(minmax.get_strategy_name(), "MinMax")

    def test_get_name_should_return_false(self):
        self.assertNotEqual(minmax.get_strategy_name(), "Hdsadasdas")

    def test_get_strategy_move_should_retun_equals(self, minmax_expected=minmax_expected_fen):
        self.chess.move("e2e4")
        boardFen = minmax.get_strategy_move()
        self.assertEquals(boardFen, minmax_expected)

    def test_get_strategy_move_should_retun__not_equals(self, minmax_expected=minmax_expected_fen):
        self.chess.move("e2e4")
        boardFen = minmax.get_strategy_move()
        self.assertEquals(boardFen, minmax_expected)

    def test_get_comment(self):
        move = self.chess.move("e2e4")
        boardFen = minmax.get_strategy_move()
        comment = minmax.get_strategy_comment(move, boardFen)
        self.assertEquals(comment, (None, None))


suite = unittest.TestLoader().loadTestsFromTestCase(minmax_test)
unittest.TextTestRunner().run(suite)
