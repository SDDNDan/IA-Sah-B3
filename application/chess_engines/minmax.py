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
    return engine.get_evaluation_depth(1), 0  # Pentru test


def get_possible_states(fen):
    """
    va returna o lista de tuple de forma (fen, mutare)
    unde fen e starea in forma fen iar mutarea este mutarea care a dus in starea aia  ( o vom folosi mai tarziu sa o returnam)
    poate fi imbunatatit daca sortam in fucntie de heuristic_eval
    """
    states = []
    for move in chess.get_valid_moves():
        chess.move(move)
        t = (chess.get_fen(), move)
        states.append(t)
        chess.undo_last_move()

    return states


def min_max(fen, depth, maximizing_player):
    if depth == 0 or is_final_state(fen):
        return heuristic_eval(fen)

    if maximizing_player:
        value = -999999999999999999
        best_move = ""
        for child, move in get_possible_states(fen):
            temp = max(value, min_max(child, depth - 1, False)[0])
            if temp > value:
                best_move = move
                value = temp
        return value, best_move
    else:
        best_move = ""
        value = 999999999999999999
        for child, move in get_possible_states(fen):
            temp = min(value, min_max(child, depth - 1, True)[0])
            if temp < value:
                value = temp
                best_move = move

        return value, best_move


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

def get_strategy_name():
    return "Minmax"


def get_strategy_move(fen):
    return min_max(fen, 2, True)[1]


def get_strategy_short_description():
    return 'Minimax is an algorithm used in artificial intelligence, decision theory, game theory, statistics and philosophy for minimizing the possible loss for a worst case (maximum loss) scenario.'


def get_strategy_description():
    return 'Minimax is an algorithm used to determine the score in a zero-sum game after a certain number of moves, with best play according to an evaluation function. The algorithm can be explained like this: In a one-ply search, where only move sequences with length one are examined, the side to move (max player) can simply look at the evaluation after playing all possible moves. The move with the best evaluation is chosen. But for a two-ply search, when the opponent also moves, things become more complicated. The opponent (min player) also chooses the move that gets the best score. Therefore, the score of each move is now the score of the worst that the opponent can do.'


def get_strategy_documentation_link():
    return 'https://www.chessprogramming.org/index.php?title=Minimax&mobileaction=toggle_view_mobile'
