import http.client
import json
import random
import sys
import time
import logging

log = logging.getLogger('grot-client')

SERVER = 'localhost'

if __name__ == '__main__':
    token = sys.argv[1]  # your Access Token
    game = sys.argv[2]  # 0 (development mode), 1 (duel), 2 (contest)

    time.sleep(random.random())

    # connect to the game server
    client = http.client.HTTPConnection(SERVER, 8080)
    client.connect()

    # block until the game starts
    client.request('GET', '/games/{}/board?token={}'.format(game, token))

    response = client.getresponse()
    '''
    {
        "score": 0,  # obtained points
        "moves": 5,  # available moves
        "moved": [None, None],  # your last choice [x, y]
        "board": [
            [
                {
                    "points": 1,
                    "direction": "up",
                    "x": 0,
                    "y": 0,
                },
                {
                    "points": 0,
                    "direction": "down",
                    "x": 1,
                    "y": 0,
                }
            ],
            [
                {
                    "points": 5,
                    "direction": "right",
                    "x": 0,
                    "y": 1,
                },
                {
                    "points": 0,
                    "direction": "left",
                    "x": 1,
                    "y": 1,
                }
            ]
        ]
    }
    '''

    while response.status == 200:
        data = json.loads(response.read().decode())

        time.sleep(random.random() * 3 + 1)

        # make your move and wait for a new round
        client.request(
            'POST', '/games/{}/board?token={}'.format(game, token),
            json.dumps({
                'x': random.randint(0, 4),
                'y': random.randint(0, 4),
            })
        )

        response = client.getresponse()