# Score categories.
# Change the values as you see fit.
from functools import wraps

YACHT = lambda d: 50 if len(set(d)) == 1 else 0
ONES = lambda d: d.count(1)
TWOS = lambda d: d.count(2) * 2
THREES = lambda d: d.count(3) * 3
FOURS = lambda d: d.count(4) * 4
FIVES = lambda d: d.count(5) * 5
SIXES = lambda d: d.count(6) * 6
FULL_HOUSE = lambda d: sum(d) if count_repeated(d) == [2, 3] else 0
FOUR_OF_A_KIND = lambda d: sorted(d)[1] * 4 if count_repeated(d)[-1] >= 4 else 0
LITTLE_STRAIGHT = lambda d: 30 if sorted(d) == [1, 2, 3, 4, 5] else 0
BIG_STRAIGHT = lambda d: 30 if sorted(d) == [2, 3, 4, 5, 6] else 0
CHOICE = sum

def count_repeated(dices):
    return sorted([dices.count(dice) for dice in set(dices)])

def score(dice, category):
    return category(dice)

