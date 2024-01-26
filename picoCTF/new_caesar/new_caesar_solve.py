from string import ascii_lowercase

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
- I can brute force the key since there are only 16 possibilities
- I need to unshift the ciphered letter and add it to a variable <- problem here cos of %
- That variable should finally be converted from hex to bytes
"""

enc: str = "mlnklfnknljflfjljnjijjmmjkmljnjhmhjgjnjjjmmkjjmijhmkjhjpmkmkmljkjijnjpmhmjjgjj"


def unshift(cipher: str) -> str:

    return ""


if __name__ == "__main__":
    print(ascii_lowercase[:16])
