from application.chess.chess_game import Chess


def get_strategy_name():
    return "Negamax"


def negamax(chess, depth, color):
    if depth == 0 or chess.is_over():
        # print(chess.get_fen())
        return color * chess.get_evaluation_depth(1), "Game over!"
    best_value = -10000000000000
    moves = chess.get_valid_moves()
    for move in moves:
        # print(move)
        chess.move(move)
        this_move_value, this_move = negamax(chess, depth - 1, -color)
        if best_value < this_move_value:
            best_value = this_move_value
            best_move = move
        chess.undo_last_move()
    return best_value, best_move


def get_strategy_move(fen):
    chess = Chess()
    chess.set_fen(fen)
    best_score, best_move = negamax(chess, 2, 1)
    return best_move
