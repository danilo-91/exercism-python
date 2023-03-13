import re

RULES = {
    r"^[aeiou]|^xr|^yt": lambda text: text + "ay",
    r"^ch|^..y|^qu|^th[^r]": lambda text: text[2:] + text[:2] + "ay",
    r"^.qu|^sch|^thr": lambda text: text[3:] + text[:3] + "ay",
    r"^.y$": lambda text: text[::-1] + "ay",
    r"^.": lambda text: text[1:] + text[0] + "ay",
}

def translate_helper(text):
    for rule, function in RULES.items():
        if re.search(rule, text):
            return function(text)

def translate(text):
    return " ".join(translate_helper(word) for word in text.split(" "))

