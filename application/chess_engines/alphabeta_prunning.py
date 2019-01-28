from application.chess.chess_game import Chess
from application.chess.engine import Engine
from application.chess.board_attributes import get_comment

print("Initializing class Engine for module " + __name__ + " ...")
engine = Engine()
print("Engine class initialized successfully!")

print("Initializing class Chess for module " + __name__ + " ...")
chess = Chess()
print("Chess class initialized successfully!")


def is_final_state(node):
    chess.set_fen(node)

    if chess.is_over():
        return True

    return False


def heuristic_eval(fen):
    engine.set_fen_position(fen)
    return engine.get_evaluation_depth(1), 0


def get_possible_states(fen):
    """
    Va returna o lista de tuple de forma (fen, mutare)
    unde fen e starea in forma fen iar mutarea este mutarea care a dus in starea aia
    (o vom folosi mai tarziu sa o returnam)
    """
    # Poate fi imbunatatit daca sortam in fucntie de heuristic_eval
    states = []
    for move in chess.get_valid_moves():
        chess.move(move)
        t = (chess.get_fen(), move)
        states.append(t)
        chess.undo_last_move()

    return states


def alpha_beta(fen, depth, alpha, beta, maximizing_player):
    if depth == 0 or is_final_state(fen):
        return heuristic_eval(fen)
    if maximizing_player:
        best_move = ""
        value = -999999999999999999
        for child, move in get_possible_states(fen):
            value = max(value, alpha_beta(
                child, depth - 1, alpha, beta, False)[0])
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
            value = min(value, alpha_beta(
                child, depth - 1, alpha, beta, True)[0])
            if value < beta:
                beta = value
                best_move = move
            if alpha >= beta:
                break  # alpha cut-off
        return value, best_move


def get_strategy_name():
    return "Alpha-Beta Pruning"


def get_strategy_move(fen):
    return alpha_beta(fen, 2, -999999999999999999, 999999999999999999, True)[1]


def get_strategy_short_description():
    return 'The alpha-beta prunning algorithm is a significant enhancement to the minmax algorithm that eliminates the need to search large portions of the game tree applying a branch-and-bound technique.'


def get_strategy_description():
    return 'The Alpha-Beta algorithm (Alpha-Beta Pruning, Alpha-Beta Heuristic) is a significant enhancement to the minimax search algorithm that  eliminates the need to search large portions of the game tree applying a branch-and-bound technique. Remarkably, it does this without any potential  of overlooking a better move. If one already has found a quite good move and search for alternatives, one refutation is enough to avoid it. No need  to look for even stronger refutations. The algorithm maintains two values, alpha and beta. They represent the minimum score that the maximizing player  is assured of and the maximum score that the minimizing player is assured of respectively. Consider checking the full documentation for more details.'


def get_strategy_documentation_link():
    return 'https://www.chessprogramming.org/Alpha-Beta'
