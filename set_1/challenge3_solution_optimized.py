from collections import Counter
from dataclasses import dataclass
from string import ascii_lowercase
from typing import Optional
from pprint import pprint

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
        # we then inject the values we got into the ScoredGuess class' constructor
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
        guess = ScoredGuess.from_key(ciphertext, candidate_key)
        # min(best_guess, guess) compares guesses by score because we passed order=True to the dataclass decorator
        best_guess = min(best_guess, guess)

    if best_guess[1] is None:
        print("There was an error. The best guess is erroneous.")
    return best_guess


# Optimized version of the scorer method
def crack_xor_cipher_faster(ciphertext: bytes) -> float:
    best_guess = ScoredGuess()

    ct_len: int = len(cipher_text)
    ct_freqs: dict = {b: ciphertext.count(b) / ct_len for b in range(256)}

    for candidate_key in range(133):
        score = 0
        for letter, frequency_expected in frequencies.items():
            score += abs(frequency_expected - ct_freqs[ord(letter) ^ candidate_key])
        guess = ScoredGuess(score, candidate_key)
        best_guess = min(best_guess, guess)

    if best_guess.key is None:
        print("Best guess has no key (This should never happen)")
    best_guess.ciphertext = ciphertext
    best_guess.plaintext = xor_buffers(ciphertext, bytes([best_guess.key]) * len(ciphertext))
    return best_guess


if __name__ == "__main__":
    cipher_text = bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
    # pprint is used here to be the ScoredGuess data type.
    pprint(crack_xor_cipher_faster(cipher_text))
