import chess


def valid_fen(fen):
    if fen is None:
        return False

    try:
        chess.Board(fen=fen)
        return True
    except:
        return False
