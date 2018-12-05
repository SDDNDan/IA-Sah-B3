from application.common_lib.package_operations import package_contents

import json

CHESS_ENGINES_PATH = '../chess_engines'


def get_strategies_controller(request):
    answer = [{"strategy": strategy} for strategy in package_contents(
        CHESS_ENGINES_PATH) if strategy != '__init__']

    return json.dumps(answer)
