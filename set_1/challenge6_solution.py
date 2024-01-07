from challenge6 import hamming_distance, ciphered_file
from itertools import combinations

# Guessing the KEYSIZE
MAX_KEYSIZE = 40


def guess_keysize(ct: bytes, num_guesses: int =1) -> list[tuple[float, int]]:
    def get_score(size: int) -> float:
        chunks = (
            ct[: size],
            ct[size: size*2],
            ct[size*2: size*3],
            ct[size*3: size*4],
        )
        avg = sum(hamming_distance(a, b) for a, b in combinations(chunks, 2)) / 6
        return avg / size

    scores = [(get_score(size), size) for size in range(1, MAX_KEYSIZE+1)]
    scores.sort()
    return scores[:num_guesses]


if __name__ == "__main__":
    print(guess_keysize(ciphered_file))




