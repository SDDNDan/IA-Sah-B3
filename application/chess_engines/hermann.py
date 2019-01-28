from application.chess.engine import Engine
from application.chess.board_attributes import get_comment

HERMANN_ENGINE_PATH = '../chess_engines_cpp/Hermann/Hermann28_64.exe'

print("Initializing class Engine for module " + __name__ + " ...")
engine = Engine(engine_path=HERMANN_ENGINE_PATH)
print("Engine class initialized successfully!")


def get_strategy_name():
    return "Hermann"


def get_strategy_move(fen):
    return engine.get_best_move(fen)


def get_strategy_comment(fen, move):
    return get_comment(engine, fen, move)


def get_strategy_short_description():
    return 'Hermann is an arena partner chess engine developed by Volker Annuss. It participated in various open computer chess championships, most notable achievement beeing third place at ICT 2009.'


def get_strategy_description():
    return 'Hermann is an arena partner chess engine developed by Volker Annuss. It participated in various open computer chess championships, most notable achievement beeing third place at ICT 2009. Hermann uses bitboards as basic data structure, determines sliding piece attacks with xed shift magic bitboards, and applies neural networks for material evaluation and timing. In 2011, Volker Annuss conrmed his soft spot for his engine names associated with the legacy of romantic German nationalism by calling Hermann\'s completely restructured successor with its Latinised name Arminius. In Germany, Arminius was rechristened Hermann (Heer Mann - army man) by Martin Luther, and he became an emblem of the revival of German nationalism fueled by the Napoleon wars in the 19th century.'


def get_strategy_documentation_link():
    return 'https://www.chessprogramming.org/Hermann'
