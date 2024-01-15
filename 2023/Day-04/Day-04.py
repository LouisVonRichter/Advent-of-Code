from utils import read_input
import re


def transformer(line):
    card_info, numbers = line.split(': ')
    card_number = int(re.findall('(\d+)', card_info)[0])
    winning, ours = numbers.split(' | ')
    winning_numbers = set([int(n) for n in re.findall(r'(\d+)', winning)])
    our_numbers = set([int(n) for n in re.findall(r'(\d+)', ours)])
    return (card_number, (winning_numbers, our_numbers))


scratch_cards = read_input(4, transformer)


def calculate_points(scratch_cards):
    points = 0
    for _id, (winning, our) in scratch_cards:
        numbers_that_won = winning & our
        if numbers_that_won:
            points += 2 ** (len(numbers_that_won) - 1)
    return points


part_1 = calculate_points(scratch_cards)
print(f'Solution: {part_1}')


def process_cards(scratch_cards):
    counts = {card_id: 1 for card_id, _ in scratch_cards}
    for card_id, (winning, our) in scratch_cards:
        numbers_that_won = winning & our
        winning_count = len(numbers_that_won)

        # I sometimes wish Python had a `times(n)` function
        # to do something n times. `range(n)` doesn't have
        # the same semantic feel

        for _ in range(counts[card_id]):
            for i in range(card_id + 1, card_id + winning_count + 1):
                counts[i] += 1
    return counts


card_counts = process_cards(scratch_cards)
part_2 = sum(c for c in card_counts.values())
print(f'Solution: {part_2}')
