from collections import Counter
from string import ascii_lowercase, ascii_letters
from challenge2_solution import xor_buffers
from codecs import decode

with open("frankenstein.txt", encoding='utf-8') as f:
    # have the book all in lowercase
    book = f.read().lower()

buffer = decode(b"1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736", "hex_codec")


# A method to get the frequency of each character in the frankenstein book
def get_freqs(txt: str, letters: str) -> dict:
    counts = Counter()
    for letter in letters:
        counts[letter] += txt.count(letter)
    total = sum(counts.values())
    # Return a dictionary of key values
    return {letter: counts[letter] / total for letter in letters}


# The reference dict that we'll use to score our plaintext
letter_freq = get_freqs(book, ascii_lowercase)


def scorer(plaintext: str) -> float:
    score = 0.0
    for letter in plaintext:
        try:
            # Sum up the values to each letter to get a final score
            score += letter_freq[letter]
        except KeyError:
            # Some keys might not be present in the ascii_letters
            continue
    return score


# We decode using only the letter characters from the string library
def decoder(ciphertext: bytes) -> str:
    result = ""
    for letter in ascii_letters:
        # Generate a 68 byte long key cast to bytes
        key = bytes(letter * 68, 'utf-8')
        if scorer(str(xor_buffers(key, ciphertext))) > 2.5:
            result = str(xor_buffers(key, ciphertext))
            print(letter, ": ", result)
    return result


print(decoder(buffer))
