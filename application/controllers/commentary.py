import json


def get_commentary_controller(request):
    game = request.args.get('game', type=str)

    if game is None:
        return 'Game sequence is needed in order to generate commentary!', 400

    ans = [
        [
            {
                "strategy": "stockfish",
                "commentary": "blablabla"
            },
            {
                "strategy": "minmax",
                "commentary": "blabla"
            }
        ],
        [
            {
                "strategy": "stockfish",
                "commentary": "blablabla"
            },
            {
                "strategy": "minmax",
                "commentary": "blabla"
            }
        ]
    ]

    return json.dumps(ans)
