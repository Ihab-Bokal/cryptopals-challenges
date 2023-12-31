"""
After some research I have figured out the following:
- Byte was quite bothering me, but what they meant is every character that is represented in ascii with 8 bits
- By single byte key they meant that the key is of the form "aaa...aaa" or "b....b", it's any character that can be represented
  with 8 bits
"""
from set_1 import challenge2_solution as c
from codecs import decode

# Ciphertext we need to decrypt
buffer = decode(b"1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736", "hex_codec")
char_freq = "etaoinshrdlu"
one_byte_chars = "!#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"


def scorer(result: str) -> int:
    letter_freq = {'a': 0, 'd': 0, 'e': 0, 'h': 0, 'i': 0,  'l': 0, 'n': 0, 'r': 0, 's': 0, 't': 0, 'o': 0, 'u': 0}
    score = 0
    for i in char_freq:
        letter_freq[i] = result.count(i)

    for char in char_freq:
        # check if the most frequent letter corresponds to the most frequent letter in the alphabet
        if max(letter_freq, key=letter_freq.get) == char:
            # If so then the score is increased by 1
            score += 1
            # We then delete that value from the dictionary to move to the next one
            del letter_freq[char]
        else:
            # We finally return the highest score that the string managed to have
            return score
    return score


# This implementation is a brute force one. After going through all outputs it turns out that X is
# the key, The encrypted message is: Cooking MC's like a pound of bacon
def decoder(inp: bytes) -> str:
    result = ""
    for i in one_byte_chars:
        # In order to convert a str to bytes we need to specify which encoding is used for that string
        key = bytes(i * 68, 'utf-8')
        # key had to be converted to bytes
        result = str(c.xor_buffers(key, inp).decode())
        if scorer(result) > -1:
            print(i + ": " + result)
    return result


print(decoder(buffer))
