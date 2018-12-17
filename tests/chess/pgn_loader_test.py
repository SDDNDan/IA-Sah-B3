import chess.pgn
import time
from anytree import Node, RenderTree

path = "../../pgns/players/Adams.pgn"


def compute_games(p_path):
    pgn = open(p_path)
    l_games = []
    l_game = chess.pgn.read_game(pgn)
    while l_game is not None:
        l_games.append(l_game)
        l_game = chess.pgn.read_game(pgn)
    return l_games


# game = chess.pgn.Game()
# game.main_line()
# root = Node("root")
# start_time = time.time()
# games = compute_games(path)
# print("Parsed games in: " + str(time.time() - start_time) + " seconds")
# start_time = time.time()
# for game in games:
#     last_node = None
#     for move in game.main_line():
#         if last_node is None:
#             if move.uci() not in root.children:
#                 last_node = Node(move.uci(), root)
#         else:
#             last_node = Node(move.uci(), last_node)
# print("Computed tree in: " + str(time.time() - start_time) + " seconds")


