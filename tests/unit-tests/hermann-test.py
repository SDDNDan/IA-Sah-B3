import unittest

from application.chess.engine import Engine
from application.chess.chess_game import Chess
from application.chess_engines import hermann

engine_path = '../../chess_engines/hermann.py'


class hermann_test(unittest.TestCase):
    chess = Chess(engine_path)
    chess.start_new_game()

    fen = "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1"

    hermann_generator_expected = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

    def test_get_name(self):
        self.assertEqual(hermann.get_strategy_name(), "Hermann")

    def test_get_name_should_return_false(self):
        self.assertNotEqual(hermann.get_strategy_name(), "Hdsadasdas")

    def test_get_strategy_move_should_retun_equals(self, hermann_generator_expected=hermann_generator_expected):
        self.chess.move("e2e4")
        boardFen = hermann.get_strategy_move()
        self.assertEquals(boardFen, hermann_generator_expected)

    def test_get_strategy_move_should_retun__not_equals(self, hermann_generator_expected=fen):
        self.chess.move("e2e4")
        boardFen = hermann.get_strategy_move()
        self.assertEquals(boardFen, hermann_generator_expected)

    def test_get_comment(self):
        move = self.chess.move("e2e4")
        boardFen = hermann.get_strategy_move()
        comment = hermann.get_strategy_comment(move, boardFen)
        self.assertEquals(comment, (None, None))




suite = unittest.TestLoader().loadTestsFromTestCase(hermann_test)
unittest.TextTestRunner().run(suite)
