import subprocess

from PYTHON.src.chess.player import Player


class Engine(Player):
    """
    AnMon - only gives best move with 'go depth 8 searchmoves'
    Herman - prints only best move
    Ruffian - prints only best move
    Rybka - like stockfish
    SOS - only gives best move
    Spike - like stockfish
    """

    def get_best_move(self, fen):
        self.set_fen_position(fen)
        return self.get_best_move_depth(1)

    def __init__(
            self, engine_path="../../../engines/stockfish-8-win/Windows/stockfish_8_x64.exe", param=None):
        if param is None:
            param = {}
        self.stockfish = subprocess.Popen(
            engine_path,
            universal_newlines=True,
            bufsize=1,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE
        )
        self.__write('uci')

        default_param = {
            'Write Debug Log': 'false',
            'Contempt': 0,
            'Min Split Depth': 0,
            'Threads': 1,
            'Ponder': 'false',
            'Hash': 16,
            'MultiPV': 1,
            'Skill Level': 20,
            'Move Overhead': 30,
            'Minimum Thinking Time': 20,
            'Slow Mover': 80,
            'UCI_Chess960': 'false'
        }

        default_param.update(param)
        self.param = default_param
        for name, value in list(default_param.items()):
            self.__set_option(name, value)

        self.__start_new_game()

    def get_evaluation_depth(self, depth):
        self.start_analyzing_depth(depth)
        return self.__read_evaluation()

    def get_evaluation_millis(self, millis):
        self.start_analyzing_millis(millis)
        return self.__read_evaluation()

    def __read_evaluation(self):
        result = ""
        while True:
            text = self.stockfish.stdout.readline().strip()
            result = result + text
            if "bestmove" in result:
                break
        return self.__parse_output_for_evaluation(result)

    @staticmethod
    def __parse_output_for_evaluation(output):
        p = output.split("cp ")
        q = p[len(p)-1].split(" ")[0]
        return int(q)/100

    def get_best_move_depth(self, depth):
        self.start_analyzing_depth(depth)
        return self.__read_best_move()

    def get_best_move_millis(self, millis):
        self.start_analyzing_millis(millis)
        return self.__read_best_move()

    def __read_best_move(self):
        """
        Returns:
            A string of move in algebraic notation or False, if it's a mate now.
        """
        while True:
            text = self.stockfish.stdout.readline().strip()
            split_text = text.split(' ')
            if split_text[0] == 'bestmove':
                if split_text[1] == '(none)':
                    return False
                return split_text[1]

    def __start_new_game(self):
        self.__write('ucinewgame')
        self.__is_ready()

    def __set_option(self, option_name, value):
        self.__write('setoption name %s value %s' % (option_name, str(value)))
        stdout = self.__is_ready()
        if stdout.find('No such') >= 0:
            print('stockfish was unable to set option %s' % option_name)

    def __is_ready(self):
        self.__write('isready')
        while True:
            text = self.stockfish.stdout.readline().strip()
            if text == 'readyok':
                return text

    def set_fen_position(self, fen_position):
        self.__write('position fen ' + fen_position)

    def start_analyzing_depth(self, depth):
        self.__write('go depth %s' % depth)

    def start_analyzing_millis(self, millis):
        self.__write('go movetime %s' % millis)

    def __write(self, command):
        self.stockfish.stdin.write(command + '\n')
        self.stockfish.stdin.flush()

    def __del__(self):
        self.stockfish.kill()
