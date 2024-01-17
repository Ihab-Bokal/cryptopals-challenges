with open("8.txt", "r") as file:
    cipher_file = [bytes(line, 'utf-8') for line in file.readlines()]


"""
Will check for repeating substrings in all of the file's lines.
The line with the most repeating substring is the one being encrypted with AES
in ECB mode.
"""


def find_rep_substring(text: bytes) -> dict[bytes, int]:
    repeating_substrs: dict[bytes, int] = {}
    # This algorithm sees strings as symmetrical data structures. If a sub str is repeated in the first half
    # There is no need to go through the second half
    for i in range(len(text) // 2 + 1, 2, -1):
        for j in range(i-1):
            sub_bytes = text[j: i]
            if text.count(sub_bytes) > 3:
                repeating_substrs[sub_bytes] = text.count(sub_bytes)
                # After finding the first substring that is repeated, no need to do through the rest
                break
    return repeating_substrs


if __name__ == "__main__":
    for i in range(len(cipher_file)):
        rep_subbytes: dict[bytes, int] = find_rep_substring(cipher_file[i])
        if b"08649af70dc06f4fd5d2d69c744cd" in rep_subbytes:
            print(i)
            print(rep_subbytes)

# Line 132 is the one containing the aes cipher in ecb mode
