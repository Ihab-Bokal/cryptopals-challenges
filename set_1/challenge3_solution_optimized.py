from collections import Counter
from dataclasses import dataclass
from string import ascii_lowercase
from typing import Optional

from challenge2_solution import xor_buffers
from challenge3_solution import book, buffer


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


@dataclass(order=True)
class ScoredGuess:
    score: float = float('inf')
    key: Optional[int] = None
    ciphertext: Optional[bytes] = None
    plaintext: Optional[bytes] = None

    @classmethod
    def from_key(cls, ctext, key_val):
        full_key = bytes([key_val]) * len(ctext)
        ptext = xor_buffers(full_key, ctext)
        score = score_text(ptext)
        return cls(score, key_val, ctext, ptext)


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
    best_guess = ScoredGuess()

    for candidate_key in range(256):
        key = bytes([candidate_key]) * len(ciphertext)
        plaintext = xor_buffers(buffer, key)
        score = score_text(plaintext)
        current_guess = (score, plaintext)
        # the min function compares the first values of the tuple and then moves to the next values
        best_guess = min(best_guess, current_guess)
    return best_guess


# print(crack_xor_cipher(buffer))
