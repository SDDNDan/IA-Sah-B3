import os

import chess
import random

from application.chess.engine import Engine


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
    def white_has_queen(board): return 'Q' in board.fen()

    @staticmethod
    def black_has_queen(board): return 'q' in board.fen()


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


def compute_random_comment(features1, features2, god_move, pleb_move):
    s1 = ' '.join(features1)
    s2 = ' '.join(features2)
    count1 = len(features1)
    count2 = len(features2)
    if count1 > 0 and count2 > 0:
        thoughts = [
            'I would rather play {} because {}, while after playing {}, the disadvantages are {}'
                .format(god_move, s1, pleb_move, s2),
            'I think {} is the best move because {}. I think your move {} is not as good because {}'
                .format(god_move, s1, pleb_move, s2),
            '{} good move. {} bad move. Get that, dum dum?'.format(god_move, pleb_move),
            'After looking at 6 million positions I concluded that {} is the best move because {}. '
            'Your move {} leads to a position where {}, which is horrible! Well... at least you are pretty.'
                .format(god_move, s1, pleb_move, s2),
            'HA! You thought {} is a good move. WRONG! Try a real move like {}: {}, but if you think that if '
            '{} gets you anywhere... uhm, well at least you can operate a computer.'.format(pleb_move, god_move, s1,
                                                                                            s2),
            'Let\'s analyze my ultimate Chad move {} vs your virgin move {}. After my god-like move, {}, while you nerd'
            ' are stuck in a position where {}. Good luck with that.'.format(god_move, pleb_move, s1, s2)
        ]
    if count1 > 0:
        thoughts = [
            'Well, after {} instead of {}, at least you get in a position where {}.'.format(god_move, pleb_move, s1)
        ]
    if count2 > 0:
        thoughts = [
            'Could you please tell me how is it good when {}. Hey, I will give you a slight hint: {} is '
            'the best move. {} might be a genius move, but this kind of genius doesn\'t play chess.'
                .format(s2, god_move, pleb_move)
        ]
    return random.choice(thoughts)


def generate_comment(fen1, fen2, engine_move, player_move):
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
    return compute_random_comment(features1, features2, engine_move, player_move)


def diff_count(f1, f2):
    count = 0
    for k in f1:
        if f1[k] != f2[k]:
            count += 1
    return count


def get_comment(engine, fen, move):
    sf = Engine('../../chess_engines_cpp/stockfish-10-win/Windows/stockfish_10_x64.exe')

    player_analysis_board = chess.Board()
    strategy_analysis_board = chess.Board()

    player_analysis_board.set_fen(fen)
    strategy_analysis_board.set_fen(fen)

    strategy_best_move = engine.get_best_move(fen)
    strategy_analysis_board.push_uci(strategy_best_move)
    player_analysis_board.push_uci(move)

    sf.set_fen_position(strategy_analysis_board.fen())
    strategy_eval = sf.get_evaluation_depth(12)

    sf.set_fen_position(player_analysis_board.fen())
    player_eval = sf.get_evaluation_depth(12)

    if abs(player_eval - strategy_eval) > 2:
        attributes1 = get_attribute_array(strategy_analysis_board.fen())
        attributes2 = get_attribute_array(player_analysis_board.fen())
        while diff_count(attributes1, attributes2) < 1:
            sf.set_fen_position(strategy_analysis_board.fen())
            strategy_analysis_board.push_uci(sf.get_best_move_depth(12))

            sf.set_fen_position(player_analysis_board.fen())
            player_analysis_board.push_uci(sf.get_best_move_depth(12))

            attributes1 = get_attribute_array(strategy_analysis_board.fen())
            attributes2 = get_attribute_array(player_analysis_board.fen())
        return generate_comment(strategy_analysis_board.fen(), player_analysis_board.fen(), strategy_best_move, move)
    return ''


if __name__ == '__main__':
    # for test
    g_fen = 'r1bqkbnr/pppp1ppp/2n5/4p3/4P3/5Q2/PPPP1PPP/RNB1KBNR w KQkq - 0 2'
    print(os.getcwd())
    g_engine = Engine(engine_path='../../chess_engines_cpp/Spike/Spike1.4.exe')
    g_comment = get_comment(g_engine, g_fen, 'f3f7')
    print(g_comment)
