from string import ascii_letters
from challenge3_solution import scorer
from challenge2_solution import xor_buffers

with open("challenge4_ciphertext.txt", encoding='utf-8') as c:
    ciphertext = c.read()
    ciphertext = bytes(ciphertext, 'utf-8')

# The full buffer's length is 333 * 60. We will go through every single set of 60 characters
# in the full_decoder function
full_buffer = ciphertext


def full_decoder(cipher: bytes) -> str:
    result = ""
    for i in range(166):
        buffer = cipher[120*i: 120*(i+1)]
        for letter in ascii_letters:
            # Generate a 68 byte long key cast to bytes
            key = bytes(letter * 68, 'utf-8')
            if scorer(str(xor_buffers(key, buffer))) > 1.5:
                result = str(xor_buffers(key, buffer))
                print(letter, ": ", result)
    return result


print(full_decoder(full_buffer))

"""
Algorithm:
- We go through every 120 characters in the file at a time because
1 character = 1 byte
2 hex characters = 1 byte
hence
60 character string = 120 character hex
- We evaluate every decoded output and if the score is greater than 1 we print out the key and the decoded string
"""
