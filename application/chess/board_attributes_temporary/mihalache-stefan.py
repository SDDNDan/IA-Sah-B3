
def white_can_castle_kingside(board):
    return 'K' in board.fen()[44:]

def black_can_castle_kingside(board):
    return 'k' in board.fen()[44:]

def white_can_castle_queenside(board):
    return 'Q' in board.fen()[44:]

def black_can_castle_queenside(board):
    return 'q' in board.fen()[44:]

def white_can_en_passant(board):
    return 'w' in board.fen()[40:] and '-' not in board.fen()[44:]

def black_can_en_passant(board):
    return 'b' in board.fen()[40:] and '-' not in board.fen()[44:]