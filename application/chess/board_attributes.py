import os

import chess
import random

from application.chess.engine import Engine
from application.chess.chess_game import Chess

SQUARES = [
    A1, B1, C1, D1, E1, F1, G1, H1,
    A2, B2, C2, D2, E2, F2, G2, H2,
    A3, B3, C3, D3, E3, F3, G3, H3,
    A4, B4, C4, D4, E4, F4, G4, H4,
    A5, B5, C5, D5, E5, F5, G5, H5,
    A6, B6, C6, D6, E6, F6, G6, H6,
    A7, B7, C7, D7, E7, F7, G7, H7,
    A8, B8, C8, D8, E8, F8, G8, H8] = range(64)

print("Initializing Engine class for board attributes ...")
sf = Engine('../chess_engines_cpp/stockfish-10-win/Windows/stockfish_10_x64.exe')
c = Chess()  # our wrapper
print("Engine class initialized successfully!")


class Attributes:
    """
    To add new attributes just add the method in this class.
    Make sure the implementation returns a boolean.
    Make the methods as specific as possible. Do not try to generalize.
    The parameter is a Board() because it is difficult to realize
    checks on a fen and calling Board::set_fen() for every attribute
    is inefficient.
    """

    @staticmethod
    def white_has_pair_of_bishops(board):
        fen = board.fen().split()[0]
        return fen.count('B') == 2 and fen.count('b') != 2

    @staticmethod
    def black_has_pair_of_bishops(board):
        fen = board.fen().split()[0]
        return fen.count('b') == 2 and fen.count('B') != 2

    @staticmethod
    def white_has_small_center_control(board):
        count = 0
        small_central_squares = [chess.E4, chess.D4, chess.E5, chess.D5]
        for sq in small_central_squares:
            if board.is_attacked_by(chess.WHITE, sq):
                count += 1
            if board.is_attacked_by(chess.BLACK, sq):
                count -= 1
        return count > 0

    @staticmethod
    def black_has_small_center_control(board):
        count = 0
        small_central_squares = [chess.E4, chess.D4, chess.E5, chess.D5]
        for sq in small_central_squares:
            if board.is_attacked_by(chess.WHITE, sq):
                count -= 1
            if board.is_attacked_by(chess.BLACK, sq):
                count += 1
        return count > 0

    @staticmethod
    def white_has_large_center_control(board):
        count = 0
        large_central_squares \
            = [chess.E4, chess.D4, chess.E5, chess.D5, chess.C3, chess.D3, chess.E3, chess.F3, chess.F4, chess.F5,
               chess.F6, chess.E6, chess.D6, chess.C6, chess.C5, chess.C4]
        for sq in large_central_squares:
            if board.is_attacked_by(chess.WHITE, sq):
                count += 1
            if board.is_attacked_by(chess.BLACK, sq):
                count -= 1
        return count > 0

    @staticmethod
    def black_has_large_center_control(board):
        count = 0
        large_central_squares \
            = [chess.E4, chess.D4, chess.E5, chess.D5, chess.C3, chess.D3, chess.E3, chess.F3, chess.F4, chess.F5,
               chess.F6, chess.E6, chess.D6, chess.C6, chess.C5, chess.C4]
        for sq in large_central_squares:
            if board.is_attacked_by(chess.WHITE, sq):
                count -= 1
            if board.is_attacked_by(chess.BLACK, sq):
                count += 1
        return count > 0

    @staticmethod
    def white_has_active_queen(board):
        for k, v in board.piece_map().items():
            if v.symbol() == 'Q' and k >= 32:
                return True
        return False

    @staticmethod
    def black_has_active_queen(board):
        for k, v in board.piece_map().items():
            if v.symbol() == 'q' and k < 32:
                return True
        return False

    @staticmethod
    def white_has_pinned_piece(board):
        for square in chess.SQUARES:
            if board.is_pinned(chess.WHITE, square):
                return True
        return False

    @staticmethod
    def black_has_pinned_piece(board):
        for square in chess.SQUARES:
            if board.is_pinned(chess.BLACK, square):
                return True
        return False

    @staticmethod
    def white_in_check(board):
        if board.turn == chess.WHITE:
            return board.is_check()
        else:
            return False

    @staticmethod
    def black_in_check(board):
        if board.turn == chess.BLACK:
            return board.is_check()
        else:
            return False

    @staticmethod
    def white_has_active_knight(board):
        for k, v in board.piece_map().items():
            if v.symbol() == 'N' and k >= 32:
                return True
        return False

    @staticmethod
    def black_has_active_knight(board):
        for k, v in board.piece_map().items():
            if v.symbol() == 'n' and k < 32:
                return True
        return False

    @staticmethod
    def white_has_active_bishop(board):
        for k, v in board.piece_map().items():
            if v.symbol() == 'B' and k >= 32:
                return True
        return False

    @staticmethod
    def black_has_active_bishop(board):
        for k, v in board.piece_map().items():
            if v.symbol() == 'b' and k < 32:
                return True
        return False

    @staticmethod
    def white_has_active_rook(board):
        for k, v in board.piece_map().items():
            if v.symbol() == 'R' and k >= 32:
                return True
        return False

    @staticmethod
    def black_has_active_rook(board):
        for k, v in board.piece_map().items():
            if v.symbol() == 'r' and k < 32:
                return True
        return False

    @staticmethod
    def white_has_advanced_pawn(board):
        for k, v in board.piece_map().items():
            if v.symbol() == 'P' and k >= 32:
                return True
        return False

    @staticmethod
    def black_has_advanced_pawn(board):
        for k, v in board.piece_map().items():
            if v.symbol() == 'p' and k < 32:
                return True
        return False

    @staticmethod
    def white_has_passing_pawn(board):
        matrix_board = get_matrix(board)
        pawn_lines = []
        pawn_columns = []

        for line in range(8):
            for column in range(8):
                if matrix_board[line][column] == 'P':
                    pawn_lines.append(line)
                    pawn_columns.append(column)
        for i in range(len(pawn_lines)):
            line = pawn_lines[i]
            column = pawn_columns[i]
            is_free = True
            for k in range(-1, 2):
                v_column = column + k
                for j in range(1, line):
                    if 0 <= v_column <= 7 and matrix_board[j][v_column] == 'p':
                        is_free = False
            if is_free:
                return True
        return False

    @staticmethod
    def black_has_passing_pawn(board):
        matrix_board = get_matrix(board)
        pawn_lines = []
        pawn_columns = []

        for line in range(8):
            for column in range(8):
                if matrix_board[line][column] == 'p':
                    pawn_lines.append(line)
                    pawn_columns.append(column)
        for i in range(len(pawn_lines)):
            line = pawn_lines[i]
            column = pawn_columns[i]
            is_free = True
            for k in range(-1, 2):
                v_column = column + k
                for j in range(line + 1, 8):
                    if 0 <= v_column <= 7 and matrix_board[j][v_column] == 'P':
                        is_free = False
            if is_free:
                return True
        return False

    @staticmethod
    def white_controls_main_diagonal_with_a_strong_bishop(board):
        matrix_board = get_matrix(board)

        for i in range(8):
            if matrix_board[i][7 - i] == 'B':
                return True
        return False

    @staticmethod
    def white_controls_secondary_diagonal_with_a_strong_bishop(board):
        matrix_board = get_matrix(board)

        for i in range(8):
            if matrix_board[i][i] == 'B':
                return True
        return False

    @staticmethod
    def black_controls_main_diagonal_with_a_strong_bishop(board):
        matrix_board = get_matrix(board)

        for i in range(8):
            if matrix_board[i][7 - i] == 'b':
                return True
        return False

    @staticmethod
    def black_controls_secondary_diagonal_with_a_strong_bishop(board):
        matrix_board = get_matrix(board)

        for i in range(8):
            if matrix_board[i][i] == 'b':
                return True
        return False

    @staticmethod
    def white_controls_open_column(board):
        matrix_board = get_matrix(board)
        for column in range(8):
            has_white_rook = False
            has_black_rook = False
            is_open = True
            for line in range(8):
                if matrix_board[line][column] == 'R':
                    has_white_rook = True
                if matrix_board[line][column] == 'r':
                    has_black_rook = True
                if matrix_board[line][column] == 'p' or matrix_board[line][column] == 'P':
                    is_open = False
            if is_open and has_white_rook and not has_black_rook:
                return True
        return False

    @staticmethod
    def black_controls_open_column(board):
        matrix_board = get_matrix(board)
        for column in range(8):
            has_white_rook = False
            has_black_rook = False
            is_open = True
            for line in range(8):
                if matrix_board[line][column] == 'R':
                    has_white_rook = True
                if matrix_board[line][column] == 'r':
                    has_black_rook = True
                if matrix_board[line][column] == 'p' or matrix_board[line][column] == 'P':
                    is_open = False
            if is_open and not has_white_rook and has_black_rook:
                return True
        return False

    @staticmethod
    def white_controls_semi_open_column(board):
        matrix_board = get_matrix(board)
        for column in range(8):
            has_white_rook = False
            has_white_pawn = False
            has_black_pawn = False

            for line in range(8):
                if matrix_board[line][column] == 'R':
                    has_white_rook = True
                if matrix_board[line][column] == 'p':
                    has_black_pawn = True
                if matrix_board[line][column] == 'P':
                    has_white_pawn = True
            if has_black_pawn and has_white_rook and not has_white_rook:
                return True
        return False

    @staticmethod
    def black_controls_semi_open_column(board):
        matrix_board = get_matrix(board)
        for column in range(8):
            has_black_rook = False
            has_white_pawn = False
            has_black_pawn = False
            for line in range(8):
                if matrix_board[line][column] == 'r':
                    has_black_rook = True
                if matrix_board[line][column] == 'P':
                    has_white_pawn = True
                if matrix_board[line][column] == 'p':
                    has_black_pawn = True
            if has_black_rook and has_white_pawn and not has_black_pawn:
                return True
        return False


"""
pioni in fata regelui
detectie deschidere
"""


# def white_knight_forks(board):

# def white_bishop_fork(board):

# def white_knight_fork(board)

# def black_bishop_fork(board):


def get_matrix(board):
    matrix = []
    for i in range(8):
        matrix.append([])
        for j in range(8):
            matrix[i].append('.')
    for k, v in board.piece_map().items():
        line = k // 8
        column = k % 8
        matrix[7 - line][column] = v.symbol()
    return matrix


if __name__ == '__main__':
    b = chess.Board()
    matrix = get_matrix(b)
    m = b.piece_map()
    print(m)


def get_attribute_array(fen):
    board = chess.Board()
    board.set_fen(fen)
    result = dict()
    for method_name in dir(Attributes):
        if not method_name.startswith("__"):
            method = getattr(Attributes, method_name)
            name = method_name.replace("_", " ")
            result[name] = method(board=board)

    return result


def compute_random_comment(features1, features2, god_move, pleb_move, color_to_move, color_not_to_move):

    s1 = ', '.join(features1)
    s2 = ', '.join(features2)

    count1 = len(features1)
    count2 = len(features2)

    if count1 > 0 and count2 > 0:
        thoughts = [
            'I would rather play {} because {}, while after playing {}, the disadvantages are {}'
                .format(god_move, s1, pleb_move, s2),
            'I think {} is the best move because {}. I think your move {} is not as good because {}'
                .format(god_move, s1, pleb_move, s2),
            # '{} good move. {} bad move. Get that, dum dum?'
            # .format(god_move, pleb_move),
            # 'After looking at 6 million positions I concluded that {} is the best move because {}. '
            # 'Your move {} leads to a position where {}, which is horrible! Well... at least you are pretty.'
            # .format(god_move, s1, pleb_move, s2),
            # 'HA! You thought {} is a good move. WRONG! Try a real move like {}: {}, but if you think that if '
            # 'a position where {} gets you anywhere... uhm, well at least you can operate a computer.'
            # .format(pleb_move, god_move, s1, s2),
            # 'Let\'s analyze my ultimate Chad move {} vs your virgin move {}. After my god-like move, {}, while you nerd'
            # ' are stuck in a position where {}. Good luck with that.'
            # .format(god_move, pleb_move, s1, s2)
        ]
    elif count1 > 0:
        thoughts = [
            'Well, after {} instead of {}, at least you get in a position where {}.'.format(
                god_move, pleb_move, s1)
        ]
    elif count2 > 0:
        thoughts = [
            'Could you please tell me how is it good when {}. Hey, I will give you a slight hint: {} is '
            'the best move. {} might be a genius move, but this kind of genius doesn\'t play chess.'
                .format(s2, god_move, pleb_move)
        ]
    else:
        thoughts = ['I can\'t explain why but my move {} is just better than your {}.'.format(
            god_move, pleb_move)
        ]

    return random.choice(thoughts)


def generate_comment(fen1, fen2, engine_move, player_move, color_to_move, color_not_to_move):
    attributes1 = get_attribute_array(fen1)
    attributes2 = get_attribute_array(fen2)
    features1 = []
    for attribute_name1, attribute_value1 in attributes1.items():
        if attribute_value1 and not attributes2[attribute_name1]:
            features1.append(attribute_name1)
    features2 = []
    for attribute_name2, attribute_value2 in attributes2.items():
        if attribute_value2 and not attributes1[attribute_name2]:
            features2.append(attribute_name2)

    features1 = [s for s in features1 if s.startswith(color_to_move)]
    features2 = [s for s in features2 if s.startswith(color_not_to_move)]

    # if len(features1) == 0 and len(features2) == 0:
    #     common = []
    #     for attribute_name1, attribute_value1 in attributes1.items():
    #         if attribute_value1 and attributes2[attribute_name1]:
    #             common.append(attribute_name1)
    #     thought = 'We both think at a position where {}, but I think that my move {} gives you the edge '\
    #         .format(', '.join(common), engine_move)
    #     return thought
    return compute_random_comment(features1, features2, engine_move, player_move, color_to_move, color_not_to_move)


def diff_count(f1, f2):
    count = 0
    for k in f1:
        if f1[k] != f2[k]:
            count += 1
    return count


def get_comment(engine, fen, move):
    c.set_fen(fen)

    player_analysis_board = chess.Board()
    strategy_analysis_board = chess.Board()

    player_analysis_board.set_fen(fen)
    strategy_analysis_board.set_fen(fen)

    if c.is_white_to_move():
        color_to_move = 'white'
        color_not_to_move = 'black'
    else:
        color_to_move = 'black'
        color_not_to_move = 'white'

    strategy_best_move = engine.get_best_move(fen)
    strategy_analysis_board.push_uci(strategy_best_move)
    player_analysis_board.push_uci(move)

    sf.set_fen_position(strategy_analysis_board.fen())
    sf.set_fen_position(player_analysis_board.fen())

    strategy_eval = -100
    try:
        strategy_eval = sf.get_evaluation_depth(12)
    except:
        print("EXCEPTION IN STRATEGY EVAL!!!")

    player_eval = -100
    try:
        player_eval = sf.get_evaluation_depth(12)
    except:
        print("EXCEPTION IN PLAYER EVAL!!!")

    if abs(player_eval - strategy_eval) > 0.4:

        # attributes1 = get_attribute_array(strategy_analysis_board.fen(), color_to_move)
        # attributes2 = get_attribute_array(player_analysis_board.fen(), color_not_to_move)
        for i in range(3):  # preferably odd number
            sf.set_fen_position(strategy_analysis_board.fen())
            strategy_analysis_board.push_uci(sf.get_best_move_depth(12))

            sf.set_fen_position(player_analysis_board.fen())
            player_analysis_board.push_uci(sf.get_best_move_depth(12))

            # attributes1 = get_attribute_array(strategy_analysis_board.fen())
            # attributes2 = get_attribute_array(player_analysis_board.fen())

        return (generate_comment(strategy_analysis_board.fen(), player_analysis_board.fen(), strategy_best_move, move,
                                 color_to_move, color_not_to_move), strategy_best_move)
    # return (None, None)


if __name__ == '__main__':
    # for test
    g_fen = 'r1bqkbnr/pppp1ppp/2n5/4p3/4P3/5Q2/PPPP1PPP/RNB1KBNR w KQkq - 0 2'
    print(os.getcwd())
    g_engine = Engine(engine_path='../../chess_engines_cpp/Spike/Spike1.4.exe')
    g_comment = get_comment(g_engine, g_fen, 'f3f7')
    print(g_comment)
