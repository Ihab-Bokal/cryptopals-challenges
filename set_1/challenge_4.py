from codecs import decode
from challenge3_solution import decoder


with open("challenge4_ciphertext.txt", encoding='utf-8') as c:
    ciphertext = c.read().lower()
    ciphertext = bytes(ciphertext, 'utf-8')

# The full buffer's length is 333 * 60. We will go through every single set of 60 characters
# in the full_decoder function
full_buffer = decode(ciphertext.hex(), "hex_codec")


def full_decoder(cipher: bytes) -> str:
    result = ""
    for i in range(333):
        result = decoder(cipher[60 * i: 60 * (i+1)])
    return result


print(full_decoder(full_buffer))
