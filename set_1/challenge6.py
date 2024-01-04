from challenge2_solution import xor_buffers
from codecs import decode
from base64 import b64decode, b64encode

# The file 6.txt is in base64
with open("6.txt") as file:
    ciphertext = bytes(file.read(), 'utf-8')


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


def find_keysize() -> tuple[int, float]:
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


# Padding function - For conversion from base64 to bytes
"""
def pad(bytes_to_pad: bytes) -> bytes:
    padded_bytes = bytes_to_pad
    if len(bytes_to_pad) % 3 == 0:
        return padded_bytes
    else:
        padding = len(bytes_to_pad) % 3 + 1
        # Replaced primitive padding ith builtin zfill()
        padded_bytes = bytes_to_pad.zfill(padding)
        return padded_bytes
"""


if __name__ == "__main__":
    # print(hamming_distance(b"wokka wokka!!!", b"this is a test")) :: Returns 37, correct answer
    print(find_keysize())

