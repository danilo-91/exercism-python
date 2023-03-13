def abbreviate(words):
    words = words.replace("-", " ").replace("_", " ").split(" ")
    return "".join(word[0] for word in words if word).upper()

