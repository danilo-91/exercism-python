# Score categories.
# Change the values as you see fit.
YACHT = lambda a: sum(a) == a*5
ONES = lambda a: a.count(1)
TWOS = lambda a: a.count(2) * 2
THREES = lambda a: a.count(3) * 3
FOURS = lambda a: a.count(4) * 4
FIVES = lambda a: a.count(5) * 5
SIXES = lambda a: a.count(6) * 6
FULL_HOUSE = lambda a: check_equality(a[:3]) and check_equality(a[3:])
FOUR_OF_A_KIND = None
LITTLE_STRAIGHT = None
BIG_STRAIGHT = None
CHOICE = None

def check_equality(list):
    return len(set(list)) == 1

def score(dice, category):
    print(dice, category)
