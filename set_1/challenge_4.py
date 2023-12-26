from challenge3_solution_optimized import crack_xor_cipher, ScoredGuess
from codecs import decode


filename = "challenge4_ciphertext.txt"
with open(filename) as file:
    lines = [line.rstrip() for line in file]


def file_decoder() -> ScoredGuess:
    result = ScoredGuess()
    for line in lines:
        # To make sure that the program is running, and there are no bugs, because it takes a lot of time to cmplete
        print(end=".", flush=True)
        cipher = decode(line, "hex")
        actual = crack_xor_cipher(cipher)
        result = min(result, actual)

    # Get the index of the ciphertext
    index = lines.index(result.ciphertext.hex())
    print("\nThe encrypted line's index: " + str(index))
    return result


if __name__ == "__main__":
    print(file_decoder())
