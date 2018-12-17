def white_has_queen(board):
        return 'Q' in board.fen()

def black_has_queen(board):
        return 'q' in board.fen()