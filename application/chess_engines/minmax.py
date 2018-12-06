from application.chess.chess_game import Chess
import copy


def get_strategy_name():
    return "MinMax"

# def get_strategy_move(fen):
#     chess = Chess()
#     chess.set_fen(fen)
#     best_move = minmax(chess)
#     return str(best_move)
#
#
# def minmax(chess, depth=1):
#     if depth == 0:
#         return
#
#     valid_moves = chess.get_valid_moves()
#     best_move = valid_moves[0]
#     best_chess = copy.copy(chess)
#     best_score = best_chess.get_best_move_depth(1)
#
#     for i in range(0, len(valid_moves)):
#         chess_clone = copy.copy(chess)
#         chess_clone.move(valid_moves[i])
#         chess_clone_score = chess_clone.get_best_move_depth(1)
#         if chess_clone_score >= best_score:
#             best_move = valid_moves[i]
#             best_score = chess_clone_score
#
#     return best_move

