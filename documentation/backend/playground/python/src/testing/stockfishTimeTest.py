import time
import matplotlib.pyplot as plt

from PYTHON.src.chess.chess_game import Chess

max_depth = 16

fens = [
    "2n5/7q/N7/b4k2/2K4p/2P1r1r1/p1R4N/B2b2Q1 w - - 0 1",
    "8/2PBk3/1R5P/p7/K1p5/1n1PP3/2N2pP1/Q5r1 w - - 0 1",
    "5b1K/pP1p1p2/p3P2p/1bN5/1np5/8/4Pk1B/8 w - - 0 1",
    "8/8/2p4P/6K1/1Pk5/8/8/6N1 w - - 0 1",
    "Nk2B1K1/5np1/4P3/1r4Rp/p2p1P1P/q4Pp1/8/8 w - - 0 1",
    "5K2/3B2N1/8/2p5/8/8/4P3/2k5 w - - 0 1",
    "5b2/8/3B4/2P5/p5K1/p6p/7R/1k6 w - - 0 1",
    "6r1/2k5/2p5/3p2p1/PP6/P7/4K3/8 w - - 0 1",
    "6k1/8/8/4P3/p2P4/K1p2P2/n2p4/8 w - - 0 1"
]

depths = []
times = []
chess = Chess()
for depth in range(1, max_depth + 1):
    print("depth: " + str(depth))
    start_time = time.time()
    for fen in fens:
        chess.get_best_move_from_fen_depth(fen, depth)
    depths.append(depth)
    total_time = time.time() - start_time
    times.append(total_time / len(fens))
plt.plot(depths, times)
plt.xlabel('depth')
plt.ylabel('time (s)')
plt.title('Stockfish')
plt.grid(True)
plt.savefig("sf.png")
plt.show()
