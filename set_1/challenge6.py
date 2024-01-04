from challenge2_solution import xor_buffers
from base64 import b64decode

# The file 6.txt is in base64
with (open("6.txt") as file):
    b64_ciphertext = bytes(file.read(), 'utf-8')
    hexed_ciphertext = b64decode(b64_ciphertext).hex()
    ciphertext = bytes(hexed_ciphertext, 'utf-8')


def hamming_distance(first_bytes: bytes, second_bytes: bytes) -> int:
    # Convert the two strs to bytes
    wokka_text = first_bytes
    test_text = second_bytes
    # XOR the two bins
    xor_result = xor_buffers(wokka_text, test_text)
    # Convert the bytes to binaries
    bin_result = ""
    # Convert each byte to binary and concatenate the binaries together
    for byte in xor_result:
        bin_result += bin(byte)[2:].zfill(8)
    # Count how many 1s are in the XOR binary result == which is the hamming distance
    hamming_dist = bin_result.count("1")
    return hamming_dist


"""------------------ STEPS ------------------
            Take first and second KEYSIZE worth of bytes
            --skip this step for now: decode them to simple bytes
            Get the hamming distance between them 
            If the hamming distance is inferior to the current keysize
        """


def find_keysizes() -> tuple[int, float]:
    # The right keysize, we'll be
    keysize: int = 0
    real_edit_distance: float = float('inf')
    for POTENTIAL_KEYSIZE in range(2, 41):
        first_bytes = ciphertext[: POTENTIAL_KEYSIZE]
        second_bytes = ciphertext[POTENTIAL_KEYSIZE: POTENTIAL_KEYSIZE * 2]
        #  Normalize the result by dividing the hamming distance by the POTENTIAL_KEYSIZE
        edit_distance = hamming_distance(first_bytes, second_bytes) / POTENTIAL_KEYSIZE
        if real_edit_distance > edit_distance:
            keysize = POTENTIAL_KEYSIZE
            real_edit_distance = edit_distance
    return keysize, real_edit_distance


"""
def find_keysize(candidates: list[int]) -> int:
    # c for candidate
    final_keysize: int = 0
    keysize_blocks: list
    for c in candidates:
        # Define the blocks of bytes that will
        keysize_blocks = [
            ciphertext[: c],
            ciphertext[c: c*2],
            ciphertext[c*2: c*3],
            ciphertext[c*3: c*4]
        ]
    return 0
"""


def break_into_blocks(keysize: int, ct: bytes) -> list[bytes]:
    # In order not to get an index out of range error
    pseudo_length = (len(ct) - (len(ct) % keysize)) // keysize
    keysize_blocks: list[bytes] = []
    for i in range(pseudo_length):
        keysize_blocks.append(ct[keysize * i: keysize * (i+1)])
    print(keysize_blocks)
    return keysize_blocks


def transpose_blocks(blocks: list[bytes]) -> list[bytes]:
    transposed_blocks: list[bytes] = []
    block_len: int = len(blocks[0])
    list_len: int = len(blocks)
    new_block: bytes = b""
    for block_parser in range(block_len):
        for list_parser in range(list_len):
            letter_byte: bytes = bytes([blocks[list_parser][block_parser]])
            new_block += letter_byte
        transposed_blocks.append(new_block)
        new_block = b""
    return transposed_blocks


if __name__ == "__main__":
    # print(hamming_distance(b"wokka wokka!!!", b"this is a test")) # Returns 37, correct answer
    print(find_keysizes())
    cipher_blocks = break_into_blocks(10, ciphertext)
    print(transpose_blocks(cipher_blocks))

