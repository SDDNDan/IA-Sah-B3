from application.chess.chess_game import Chess
from application.chess.board_attributes import get_comment

print("Initializing class Chess for module " + __name__ + " ...")
chess = Chess()
print("Chess class initialized successfully!")


def negamax(chess, depth, color):
    if depth == 0 or chess.is_over():
        return color * chess.get_evaluation_depth(1), "Game over!"

    best_value = -10000000000000
    moves = chess.get_valid_moves()
    for move in moves:
        chess.move(move)
        this_move_value, this_move = negamax(chess, depth - 1, -color)
        if best_value < this_move_value:
            best_value = this_move_value
            best_move = move
        chess.undo_last_move()
    return best_value, best_move


def get_strategy_name():
    return "Negamax"


def get_strategy_move(fen):
    chess.set_fen(fen)
    best_score, best_move = negamax(chess, 2, 1)
    return best_move


def get_strategy_short_description():
    return 'Negamax is a common way of implementing minimax and derived algorithms. Instead of using two separate subroutines for the Min player and the Max player, it passes on the negated score due to a mathematical relationship.'


def get_strategy_description():
    return 'Negamax is a common way of implementing minimax and derived algorithms. Instead of using two separate subroutines for the Min player and the Max player, it passes on the negated score due to following mathematical relation: max(a, b) == -min(-a, -b)'


def get_strategy_documentation_link():
    return 'https://www.chessprogramming.org/Negamax'
