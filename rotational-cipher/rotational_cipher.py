LOWER_ALPHABET = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABET = LOWER_ALPHABET.upper()

def rotate_letter(char, key):
    if char.isalpha():
        if char in LOWER_ALPHABET:
            new_index = (LOWER_ALPHABET.find(char) + key) % len(LOWER_ALPHABET)
            return LOWER_ALPHABET[new_index]

        if char in UPPER_ALPHABET:
            new_index = (UPPER_ALPHABET.find(char) + key) % len(UPPER_ALPHABET)
            return UPPER_ALPHABET[new_index]

        return char

    return char

def rotate(text, key):
    return "".join(rotate_letter(char, key) for char in text)

