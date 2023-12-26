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


def find_keysize():
    for KEYSIZE in range(2, 41):
        print("first KEYSIZE worth of bytes: " + b64decode(ciphertext[:KEYSIZE*12]).hex())
        print("second KEYSIZE worth of bytes: " + b64decode(ciphertext[KEYSIZE*12:KEYSIZE*24]).hex())
        if KEYSIZE == 4:
            break
    return 0


if __name__ == "__main__":
    print(hamming_distance(b"wokka wokka!!!", b"this is a test"))
    find_keysize()

