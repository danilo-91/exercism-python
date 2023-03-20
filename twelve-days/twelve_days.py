DAYS = [
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth",
]

GIFTS = [
    "and a Partridge in a Pear Tree.",
    "two Turtle Doves,",
    "three French Hens,",
    "four Calling Birds,",
    "five Gold Rings,",
    "six Geese-a-Laying,",
    "seven Swans-a-Swimming,",
    "eight Maids-a-Milking,",
    "nine Ladies Dancing,",
    "ten Lords-a-Leaping,",
    "eleven Pipers Piping,",
    "twelve Drummers Drumming,",
]

PARTRIDGE = "a Partridge in a Pear Tree."

def verse(day, gift):
    return f"On the {day} day of Christmas my true love gave to me: {gift}"

def recite(start_verse, end_verse):
    verses = []

    for i in range(start_verse - 1, end_verse):
        if i == 0:
            verses.append(verse(DAYS[i], PARTRIDGE))
            continue
        verses.append(verse(DAYS[i], " ".join(GIFTS[:i+1][::-1])))

    return verses
