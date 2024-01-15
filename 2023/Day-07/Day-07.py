from utils import read_input
from collections import Counter
from enum import Enum


class HandValue(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIRS = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7


NUMERIC_VALUES = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}


class Hand:

    def __init__(self, cards):
        self.cards = list(cards)
        self.card_set = set(cards)
        self.card_counts = Counter(cards)
        self.value = self.get_value()
        self.numeric_values = NUMERIC_VALUES

    def is_five_of_a_kind(self):
        return len(self.card_set) == 1

    def is_four_of_a_kind(self):
        if len(self.card_set) != 2:
            return False
        return any(c for c in self.card_counts.values() if c == 4)

    def is_full_house(self):
        has_triplet = any(c for c in self.card_counts.values() if c == 3)
        has_pair = any(c for c in self.card_counts.values() if c == 2)
        return has_triplet and has_pair

    def is_three_of_a_kind(self):
        return any(c for c in self.card_counts.values() if c == 3)

    def is_two_pairs(self):
        pairs = [c for c in self.card_counts.values() if c == 2]
        return len(pairs) == 2

    def is_one_pair(self):
        pairs = [c for c in self.card_counts.values() if c == 2]
        return len(pairs) == 1

    def get_value(self):
        if self.is_five_of_a_kind():
            return HandValue.FIVE_OF_A_KIND
        if self.is_four_of_a_kind():
            return HandValue.FOUR_OF_A_KIND
        if self.is_full_house():
            return HandValue.FULL_HOUSE
        if self.is_three_of_a_kind():
            return HandValue.THREE_OF_A_KIND
        if self.is_two_pairs():
            return HandValue.TWO_PAIRS
        if self.is_one_pair():
            return HandValue.ONE_PAIR

        return HandValue.HIGH_CARD

    def __lt__(self, other):
        if self.value.value != other.value.value:
            return self.value.value < other.value.value
        else:
            for c1, c2 in zip(self.cards, other.cards):
                c1_value = self.numeric_values[c1]
                c2_value = self.numeric_values[c2]
                if c1_value == c2_value:
                    continue
                return c1_value < c2_value

    def __repr__(self):
        return f'<Hand: {"".join(self.cards)} {self.value}>'


def transformer(line):
    hand, bid = line.split(' ')
    hand = Hand(hand)
    bid = int(bid)
    return hand, bid


hands = read_input(7, transformer)

part_1 = 0
for i, (hand, bid) in enumerate(sorted(hands)):
    part_1 += (i+1) * bid
print(part_1)


JOKER_NUMERIC_VALUES = NUMERIC_VALUES.copy()
JOKER_NUMERIC_VALUES['J'] = 0


class JokerHand(Hand):

    def __init__(self, cards):
        self.joker = 'J' in cards
        super().__init__(cards)
        self.numeric_values = JOKER_NUMERIC_VALUES

    def is_five_of_a_kind(self):
        if not self.joker:
            return len(self.card_set) == 1
        return len(self.card_set) <= 2

    def is_four_of_a_kind(self):
        if not self.joker:
            if len(self.card_set) != 2:
                return False
            return any(c for c in self.card_counts.values() if c == 4)
        return any(count for card, count in self.card_counts.items() if count == 4 - self.cards.count('J') and card != 'J')

    def is_full_house(self):
        has_triplet = any(c for c in self.card_counts.values() if c == 3)
        has_pair = any(c for c in self.card_counts.values() if c == 2)
        full_house = has_triplet and has_pair
        if full_house:
            return True
        elif not full_house and not self.joker:
            return False
        else:  # Not a natural full house but has joker so it might still be
            pairs = [card for card, count in self.card_counts.items()
                     if count == 2]
            return len(pairs) == 2

    def is_three_of_a_kind(self):
        return any(c for c in self.card_counts.values() if c == 3 - self.cards.count('J'))

    def is_one_pair(self):
        if self.joker:
            return True
        pairs = [c for c in self.card_counts.values() if c == 2]
        return len(pairs) == 1


def transformer(line):
    hand, bid = line.split(' ')
    hand = JokerHand(hand)
    bid = int(bid)
    return hand, bid


jokerhands = read_input(7, transformer)

part_2 = 0
for i, (hand, bid) in enumerate(sorted(jokerhands)):
    part_2 += (i+1) * bid
print(part_2)
