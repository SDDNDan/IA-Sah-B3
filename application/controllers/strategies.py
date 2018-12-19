from application.common_lib.package_operations import list_package_modules
import json

CHESS_ENGINES_PACKAGE_NAME = 'application.chess_engines'


def get_strategies_controller(request):
    answer = [{"strategy": strategy.split(".")[-1]}
              for strategy in list_package_modules(CHESS_ENGINES_PACKAGE_NAME)]

    return json.dumps(answer)
