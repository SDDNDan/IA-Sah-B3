import chess

def white_has_passing_pawns(board):
    matrix_board = []chess.Board(board.fen())
    # print(chess.Board( "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"))#board.fen())
    for col in range(8):
        black_pawn = 0
        white_pawn = 0
        for lin in range(8):
            if matrix_board[lin][col] == 'p':
                black_pawn = 1
            elif matrix_board[lin][col] == 'P':
                white_pawn = 1
        if white_pawn and !black_pawn:
            return True
    return False 

def black_has_passing_pawns(board):
    matrix_board = chess.Board(board.fen())
    for col in range(8):
        black_pawn = 0
        white_pawn = 0
        for lin in range(8):
            if matrix_board[lin][col] == 'p':
                black_pawn = 1
            elif matrix_board[lin][col] == 'P':
                white_pawn = 1
        if !white_pawn and black_pawn:
            return True
    return False

def white_has_taken_diagonal(board):
    matrix_board = chess.Board(board.fen())
    for i in range(8):
        if matrix_board[i][i] == 'B':
            return True
        if matrix_board[i][7-i] == 'B'
            return True
    return False

def black_has_taken_diagonal(board):
    matrix_board = chess.Board(board.fen())
    for i in range(8):
        if matrix_board[i][i] == 'b':
            return True
        if matrix_board[i][7-i] == 'b'
            return True
    return False

def white_has_pinned_piece(board):
    for square in chess.SQUARES:
        if board.is_pinned(chess.WHITE, square)
            return True
    return False

def black_has_pinned_piece(board):
    for square in chess.SQUARES:
        if board.is_pinned(chess.BLACK, square)
            return True
    return False

def white_in_check(board)
    if board.turn == chess.WHITE:
        return board.is_check()

def black_in_check(board)
    if board.turn == chess.BLACK:
        return board.is_check()

# def white_knight_forks(board):

# def white_bishop_fork(board):

# def white_knight_fork(board)

# def black_bishop_fork(board):

# def white_has_promoted_pawns(board):

# def black_has_promoted_pawns(board):

# def white_in_zugzwang(board):

# def black_in_zugzwang(board):