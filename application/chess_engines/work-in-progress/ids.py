from application.chess.engine import Engine
from application.chess.chess_game import Chess
from application.chess.board_attributes import get_comment

print("Initializing class Engine for module " + __name__ + " ...")
engine = Engine()
print("Engine class initialized successfully!")

print("Initializing class Chess for module " + __name__ + " ...")
chess = Chess()
print("Chess class initialized successfully!")

MAX_DEPTH = 10


def get_strategy_name():
    return "Iterative deepening search"


def get_strategy_move(fen):
    return "d2d4"


def is_final_state(node):
    """
    Verifica daca o stare este stare finala adica daca cineva castiga jocul
    """
    return False


def heuristic_eval(fen):
    """
    #  Returneaza evaluarea unei stari
    """
    engine.set_fen_position(fen)
    engine.get_evaluation_depth(1)


def get_possible_states(fen):
    """
    va returna o lista de tuple de forma (fen, mutare)
    unde fen e starea in forma fen iar mutarea este mutarea care a dus in starea aia
    ( o vom folosi mai tarziu sa o returnam)
    poate fi imbunatatit daca sortam in fucntie de heuristic_eval
    """

    states = []
    for move in chess.get_valid_moves():
        chess.move(move)
        t = tuple(chess.get_fen(), move)
        states.append(t)
        chess.undo_last_move()

    return states


def ids(fen, depth, maximizing_player, goal):
    if depth == 0 or is_final_state(fen):
        return heuristic_eval(fen)

    maxim = -999999999999999999
    minim = 999999999999999999

    if depth == MAX_DEPTH:
        for child, move in get_possible_states(fen):
            val, bm, ok = ids(child, depth - 1, True, goal)
            if ok:
                return val, bm, ok

    if maximizing_player:
        best_move = ""
        value = -999999999999999999
        for child, move in get_possible_states(fen):
            val, bm, ok = ids(child, depth - 1, True, goal)
            if ok:
                return val, bm, ok
        for child, move in get_possible_states(fen):
            value = max(value, ids(child, depth - 1, False, goal)[0])
            if value > maxim:
                maxim = value
                best_move = move
            if maxim > goal:
                return value, best_move, True
        return value, best_move, False
    else:
        best_move = ""
        value = 999999999999999999
        for child, move in get_possible_states(fen):
            val, bm, ok = ids(child, depth - 1, True, goal)
            if ok:
                return val, bm, ok
        for child, move in get_possible_states(fen):
            value = min(value, ids(child, depth - 1, True, goal)[0])
            ok = max(0, ids(child, depth - 1, True, goal)[2])
            if value < minim:
                minim = value
                best_move = move
        return value, best_move, False


def get_strategy_comment(fen, move):
    return get_comment(engine, fen, move)
