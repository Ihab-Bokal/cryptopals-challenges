from challenge3_solution_optimized import crack_xor_cipher
from codecs import decode

with open("challenge4_ciphertext.txt", encoding='utf-8') as c:
    ciphertext = c.read()
    ciphertext = bytes(ciphertext, 'utf-8')

# The full buffer's length is 333 * 60. We will go through every single set of 60 characters
# in the full_decoder function
full_buffer = decode(ciphertext.hex(), "hex_codec")


def full_decoder(cipher: bytes) -> tuple[float, bytes, int]:
    # a tuple containing he score and the according plaintext and the line containing the ciphertext
    result = (float('inf'), None, 0)
    for i in range(327):
        # Load lines from the encrypted file one after one using get_chars()
        buffer = get_chars(full_buffer[61*i:])
        main_tuple = crack_xor_cipher(buffer)
        current_result = (main_tuple[0], main_tuple[1], i)
        # Keep only results with the lowest score
        if result[0] > current_result[0]:
            result = current_result
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


print(full_decoder(full_buffer))
