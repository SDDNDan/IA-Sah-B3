from application.chess.engine import Engine
from application.chess.chess_game import Chess

def get_strategy_name():
    return "Alpha-beta prunning"

#  verifica daca o stare este stare finala adica daca cineva castiga jocul
def is_final_state(node):
    return False


#  Returneaza evaluarea unei stari

def heuristic_eval(fen):
    engine = Engine()
    engine.set_fen_position(fen)
    engine.get_evaluation_depth(1)

    

#  va returna o lista de tuple de forma (fen, mutare)
#  unde fen e starea in forma fen iar mutarea este mutarea care a dus in starea aia  ( o vom folosi mai tarziu sa o returnam)
def get_possible_states(fen):
    #  poate fi imbunatatit daca sortam in fucntie de heuristic_eval
    chess = Chess()
    states = []
    for move in chess.get_valid_moves():
        chess.move(move)
        t = tuple(chess.get_fen(), move)
        states.append(t)
        chess.undo_last_move()

    return states

"""
Acum ca ma gandesc mai bine, stockfish deja foloseste alpha beta prunging, 
asa ca mm fi putut cheam direct engine.get_evaluation_depth(adamcimea_dorita)
"""
def alpha_beta(fen, depth, alpha, beta, maximizing_player):
    if depth == 0 or is_final_state(fen):
        return heuristic_eval(fen)

    if maximizing_player:
        best_move = ""
        value = -999999999999999999

        for child, move in get_possible_states(fen):
            value = max(value, alpha_beta(child, depth - 1, alpha, beta, False))
            if value > alpha:
                alpha = value
                best_move = move
            if alpha >= beta:
                break  # beta cut-off
        return value, best_move
    else:
        best_move = ""
        value = 999999999999999999
        for child, move in get_possible_states(fen):
            value = min(value, alpha_beta(child, depth - 1, alpha, beta, True))
            if value < beta:
                beta = value
                best_move = move
            if alpha >= beta:
                break  # alpha cut-off
        return value, best_move


def get_strategy_move(fen):
    return alpha_beta(fen, 10, -999999999999999999, 999999999999999999, True)[1]
    # return "D2D4"
