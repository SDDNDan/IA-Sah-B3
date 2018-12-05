from application.chess.engine import Engine

fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'

engines = [
    Engine('../../chess_engines_cpp/stockfish-10-win/Windows/stockfish_10_x64.exe'),
    Engine('../../chess_engines_cpp/stockfish-9-win/Windows/stockfish_9_x64.exe'),
    Engine('../../chess_engines_cpp/stockfish-8-win/Windows/stockfish_8_x64.exe'),
    Engine('../../chess_engines_cpp/Spike/Spike1.4.exe'),
    Engine('../../chess_engines_cpp/SOS/SOS-51_Arena.exe'),
    Engine('../../chess_engines_cpp/Rybka/Rybkav2.3.2a.mp.x64.exe'),
    Engine('../../chess_engines_cpp/Ruffian/Ruffian_105.exe'),
    Engine('../../chess_engines_cpp/Hermann/Hermann28_64.exe'),
    Engine('../../chess_engines_cpp/AnMon/AnMon_5.75.exe')
]

errors = []

for engine in engines:
    name = engine.get_engine_name()
    move = None
    score = None
    try:
        move = engine.get_best_move(fen)
    except ValueError:
        error = name + " could not compute move"
        errors.append(error)
    try:
        score = engine.get_evaluation_millis(100)
    except ValueError:
        error = name + " could not compute position evaluation"
        errors.append(error)
    print(name + ": best move=\'" + str(move) + "\' eval=\'" + str(score) + "\'")

for error in errors:
    print(error)
