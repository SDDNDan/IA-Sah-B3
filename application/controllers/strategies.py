from application.common_lib.package_operations import list_package_modules
import json
import importlib

CHESS_ENGINES_PACKAGE_NAME = 'application.chess_engines'


def get_strategies_controller(request):
    answer = []

    for chess_engine_module_name in list_package_modules(CHESS_ENGINES_PACKAGE_NAME):
        chess_engine_module = importlib.import_module(
            chess_engine_module_name)

        answer.append({
            'strategy': chess_engine_module_name.split(".")[-1],
            'strategyPrettyName': chess_engine_module.get_strategy_name(),
            'shortDescription': chess_engine_module.get_strategy_short_description(),
            'description': chess_engine_module.get_strategy_description(),
            'documentation': chess_engine_module.get_strategy_documentation_link()
        })

    return json.dumps(answer)
