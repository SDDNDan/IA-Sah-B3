import chess.pgn
import os
import chess

from PYTHON.src.chess.chess_game import Chess


def get_fens_from_moves(move_list):
    l_fens = set()
    l_chess = Chess()
    for move in move_list:
        l_chess.move(str(move))
        l_fens.add(l_chess.get_fen())
    return l_fens


def get_fens_from_pgn_file(path):
    l_fens = set()
    with open(path) as pgn:
        l_game = chess.pgn.read_game(pgn)
        while l_game is not None:
            moves = l_game.main_line()
            l_fens.update(get_fens_from_moves(moves))
            l_game = chess.pgn.read_game(pgn)
    return l_fens


def get_fens_from_fen_file(path, max_fen_count):
    l_fens = set()
    with open(path) as file:
        line = file.readline()
        count = 0
        while line is not None and count < max_fen_count:
            l_fens.add(line[:-5])
            line = file.readline()
            count += 1
    return l_fens


def get_fens_recursively(p_search_root, max_fen_count_per_file):
    l_fens = set()
    for (root, directories, files) in os.walk(p_search_root):
        for file_name in files:
            full_file_path = os.path.join(root, file_name)
            l_fens = get_fens_from_fen_file(full_file_path, max_fen_count_per_file)
            l_fens.update(l_fens)
            # print(full_file_path)
    return l_fens


search_root = "../../data/fens/players"
fens = get_fens_recursively(search_root, 50)
