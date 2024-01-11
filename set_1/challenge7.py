from base64 import b64decode
from challenge2_solution import xor_buffers


# 7.txt has been b64 encoded and encrypted with AES-128 in ECB mode under the key "YELLOW SUBMARINE"
with open("7.txt", "r") as file:
    encoded_text = file.read().replace('\n', '')
    ciphered_file = b64decode(encoded_text)

"""
ABOUT AES:
AES uses a SPN (substitution-permutation network) to encrypt the data based on a 4x4 matrix
DES which is AES' predecessor used to work with Feistel network.

AES-128-EBC means that the key length is 128 bytes => the key is "YELLOW SUBMARINE" * 8.

ECB mode:
you just break pt into blocks to cipher it to vice versa
"""


# Return a list of blocks where each element is of length 16bytes
def break_blocks(ct: bytes) -> list[bytes]:
    blocks: list[bytes] = []

    for i in range(len(ct) // 16):
        blocks.append(ct[16*i: 16*(i+1)])

    return blocks


def break_aes_ecb(ct_blocks: list[bytes], k: bytes) -> bytes:
    pt: bytes = b""
    pt_part: bytes

    for block in ct_blocks:
        pt_part = xor_buffers(block, k)
        pt += pt_part

    return pt


if __name__ == "__main__":
    cipherBlocks = break_blocks(ciphered_file)
    key: bytes = b"YELLOW SUBMARINE"
    print(break_aes_ecb(cipherBlocks, key))
