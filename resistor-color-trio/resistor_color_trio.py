RESISTORS = {
    "black":    0,
    "brown":    1,
    "red":      2,
    "orange":   3,
    "yellow":   4,
    "green":    5,
    "blue":     6,
    "violet":   7,
    "grey":     8,
    "white":    9,
}

METRIC = [
    ("giga", 10 ** 9),
    ("mega", 10 ** 6),
    ("kilo", 10 ** 3),
]

def label(colors):
    digit1, digit2, exponent = [RESISTORS[color] for color in colors][0:3]
    prefix = ""
    num = (digit1 * 10 + digit2) * 10 ** exponent

    for metric, value in METRIC:
        if num >= value:
            prefix = metric
            num = num // value

    return f"{num} {prefix}ohms"

