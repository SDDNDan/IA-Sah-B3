import chess


def valid_fen(fen):
    try:
        chess.Board(fen=fen)
        return True
    except:
        return False
