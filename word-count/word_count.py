import re

def split_words(sentence):
    # re means letter apostrophe letter or any alphanumeric
    return re.findall("[a-z]+'[a-z]+|[a-z0-9]+", sentence.lower())

def count_words(sentence):
    words = split_words(sentence)
    return {word: words.count(word) for word in words}
