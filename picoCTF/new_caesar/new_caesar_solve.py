from string import ascii_lowercase
from base64 import b16decode, b16encode

LOWERCASE_OFFSET = ord("a")
# lowercase letters from a to p
ALPHABET = ascii_lowercase[:16]

"""
ciphering reqs:
1. Key should be single byte
2. Flag has to be hex encoded
3. every character of the encoded flag is shifted by the single character
the catch is that the cipher contains only characters between a and p. and that the shift 
function has a modulus in it so it's circular

Encryption steps:
1. Encode the flag in base16
2. shift every character in the b16_flag by key[i % len(key)] / i = character's index

CC:
- brute force the key : there are 16 possible values
- unshift the ciphered letter and add it to a variable
- That variable should finally be converted from hex to bytes
"""

flag: bytes = b"mlnklfnknljflfjljnjijjmmjkmljnjhmhjgjnjjjmmkjjmijhmkjhjpmkmkmljkjijnjpmhmjjgjj"


def unshift(cipher_char: chr, k: chr):
    # Convert to the index of the ascii_lowercase string
    t1: int = ord(cipher_char) - LOWERCASE_OFFSET
    t2: int = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 - t2) % len(ALPHABET)]


if __name__ == "__main__":
    print("[+] --- Breaking new caesar --- [+]")
    dec = ""

    for key in ascii_lowercase[:16]:
        for i, c in enumerate(b16encode(flag)):
            print(type(c))
            dec += unshift(c, key)

    b16decode(dec)
    # for i, c in enumerate(b16):
    #     enc += shift(c, key[i % len(key)])

