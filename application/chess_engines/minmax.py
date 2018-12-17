from application.chess.chess_game import Chess
from application.chess.engine import Engine

import copy


def get_strategy_name():
    return "MinMax"


def get_strategy_move(fen):
    return min_max(fen, 2, True, Engine(), Chess())[1]


def is_final_state(node, chess):
    chess.set_fen(node)
    if chess.is_over():
        return True
    return False


def heuristic_eval(fen, engine):
    engine.set_fen_position(fen)
    # print(engine.get_evaluation_depth(1))
    return engine.get_evaluation_depth(1), 0  # Pentru test


def get_possible_states(fen, chess):
    #
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


def min_max(fen, depth, maximizing_player, engine, chess):
    if depth == 0 or is_final_state(fen, chess):
        return heuristic_eval(fen, engine)

    if maximizing_player:
        value = -999999999999999999
        best_move = "e2e4"
        for child, move in get_possible_states(fen, chess):
            temp = min_max(child, depth - 1, False, engine, chess)[0]
            if value > temp:
                best_move = move
                value = temp
        return value, best_move
    else: 
        best_move = "e2e4"
        value = 999999999999999999
        for child, move in get_possible_states(fen, chess):
            temp = min_max(child, depth - 1, True, engine, chess)[0]
            if value < temp:
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



