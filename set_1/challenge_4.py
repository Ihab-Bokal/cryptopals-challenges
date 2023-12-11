from string import ascii_uppercase
from challenge3_solution import scorer
from challenge2_solution import xor_buffers
from codecs import decode

with open("challenge4_ciphertext.txt", encoding='utf-8') as c:
    ciphertext = c.read()
    ciphertext = bytes(ciphertext, 'utf-8')

# The full buffer's length is 333 * 60. We will go through every single set of 60 characters
# in the full_decoder function
full_buffer = decode(ciphertext.hex(), "hex_codec")
# print full_buffer in its byte format
# print(full_buffer)


def full_decoder(cipher: bytes) -> str:
    result = ""
    for i in range(327):
        # Load lines from the encrypted file one after one using get_chars()
        buffer = get_chars(full_buffer[61*i:])
        for letter in ascii_uppercase:
            # Generate a 60 byte long key cast to bytes to get the key
            key = bytes(letter * 60, 'utf-8')
            if scorer(str(xor_buffers(key, buffer))) > 1:
                result = str(xor_buffers(key, buffer))
                print(letter, ": ", result)
    return result


# define a method that gets values until it finds a line break, the output should
def get_chars(inp: bytes) -> bytes:
    output: str = ""
    for i in str(inp):
        if i != '\\':
            output += i
        else:
            return bytes(output, 'utf-8')[2:]
    return bytes(output, 'utf-8')[2:]


# print(get_chars(full_buffer))
print(full_decoder(full_buffer))
"""
Algorithm:
- We go through every 60 characters in the file at a time because
1 character = 1 byte
2 hex characters = 1 byte
hence
60 character string = 120 character hex
- We evaluate every decoded output and if the score is greater than 1 we print out the key and the decoded string
"""
