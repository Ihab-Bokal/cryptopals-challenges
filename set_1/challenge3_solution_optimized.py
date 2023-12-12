from collections import Counter
from string import ascii_lowercase
from challenge2_solution import xor_buffers
from codecs import decode


with open("frankenstein.txt", encoding='utf-8') as f:
    # have the book all in lowercase
    book = f.read().lower()

buffer = decode(b"1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736", "hex_codec")


# A method to get the frequency of each character in the frankenstein book
def get_frequencies(txt: str, letters: str) -> dict:
    counts = Counter()
    for letter in letters:
        # We will only score based on lowercase letters because they're more frequent
        # Taking uppercase chars into account will have our result be misplaced
        counts[letter] += txt.count(letter)
    total = sum(counts.values())
    # Return a dictionary of key values
    return {letter: counts[letter] / total for letter in letters}


# Have a dictionary with the letters as keys and their frequencies as values
frequencies = get_frequencies(book, ascii_lowercase)


def score_text(text: bytes) -> float:
    # lower scores are better
    score = 0.0
    l = len(text)

    for letter, frequency_expected in frequencies.items():
        # ord(char) takes a char and returns its Unicode code. ord('a') = 97.
        # count(ord(letter)) because text is in bytes and all of its chars are in Unicode code
        frequency_actual = text.count(ord(letter)) / l
        err = abs(frequency_expected - frequency_actual)
        # The closer the score is to zero, the more probable our decrypted text is to be right
        score += err
    return score


def crack_xor_cipher(ciphertext: bytes) -> tuple[float, bytes]:
    #  The form of best_guess is (score, plaintext)
    best_guess = (float('inf'), b"")

    for i in range(256):
        key = bytes([i]) * len(ciphertext)
        plaintext = xor_buffers(buffer, key)
        score = score_text(plaintext)
        current_guess = (score, plaintext)
        # the min function compares the first values of the tuple and then moves to the next values
        best_guess = min(best_guess, current_guess)
    return best_guess


# print(crack_xor_cipher(buffer))
