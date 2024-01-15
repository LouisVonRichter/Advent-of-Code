import re
from collections import namedtuple

from utils import read_input


PULLED_CUBES_PATTERN = r'((\d+) (blue|red|green))+'

Game = namedtuple('Game', ['id', 'rounds'])
Round = namedtuple('Round', ['blue', 'red', 'green'])


def transformer(line):
    game_input, rounds_input = line.split(': ')
    game_id = game_input.strip().split(' ')[1]
    rounds = [round.strip() for round in rounds_input.split(';')]
    rounds_in_game = []

    for round in rounds:
        current_round = Round(blue=0, red=0, green=0)
        for matches in re.findall(PULLED_CUBES_PATTERN, round):
            # Filter out missing cube colors
            _, count, color = matches

            # Create a dictionary that can be used as **kwargs to `_replace` method
            update = {color: int(count)}
            current_round = current_round._replace(**update)

            rounds_in_game.append(current_round)
    game = Game(id=int(game_id), rounds=rounds_in_game)

    return game


games = read_input(2, transformer)


def validate(games):
    MAX_RED = 12
    MAX_GREEN = 13
    MAX_BLUE = 14
    valid_games = []
    for game in games:
        is_valid = True
        for round in game.rounds:
            if round.blue > MAX_BLUE or round.red > MAX_RED or round.green > MAX_GREEN:
                break
        else:
            valid_games.append(game)
    return sum(game.id for game in valid_games)


part_1 = validate(games)
print(f'Solution: {part_1}')


def calculate_power(game):
    min_green = max(round.green for round in game.rounds)
    min_blue = max(round.blue for round in game.rounds)
    min_red = max(round.red for round in game.rounds)
    return min_green * min_blue * min_red


def calculate_total_power(games):
    return sum(calculate_power(game) for game in games)


part_2 = calculate_total_power(games)
print(f'Solution: {part_2}')
