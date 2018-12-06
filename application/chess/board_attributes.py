import chess


class Attributes:
    """
    To add new attributes just add the method in this class.
    Make sure the implementation returns a boolean.
    Make the methods as specific as possible. Do not try to generalize.
    The parameter is a Board() because it is difficult to realize
    checks on a fen and calling Board::set_fen() for every attribute
    is inefficient.
    """

    @staticmethod
    def white_has_queen(board): return 'Q' in board.fen()

    @staticmethod
    def black_has_queen(board): return 'q' in board.fen()


def get_attribute_array(fen):
    board = chess.Board()
    board.set_fen(fen)
    result = dict()
    for method_name in dir(Attributes):
        if not method_name.startswith("__"):
            method = getattr(Attributes, method_name)
            name = method_name.replace("_", " ")
            result[name] = method(board=board)
    return result


# for test
attributes = get_attribute_array(chess.Board().fen())
for attribute_name, attribute_value in attributes.items():
    print(attribute_name + " = " + str(attribute_value))
