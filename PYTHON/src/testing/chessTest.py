from PYTHON.src.chess.chess_game import Chess

chess = Chess()
chess.move("e2e4")
print(chess.get_best_move_depth(12))
print(chess.get_evaluation_depth(15))
