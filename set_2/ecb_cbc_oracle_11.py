from implement_cbc_10 import aes_cbc_enc, aes_ecb_enc, aes_ecb_dec
from random import randbytes, randint
from pkcs7_09 import pkcs7
from os import urandom

"""
Now that you have ECB and CBC working:

1- Write a function to generate a random AES key; that's just 16 random bytes.
2- Write a function that encrypts data under an unknown key --- that is, a function that generates a random key and encrypts under it.
3. Function appends 5-10 bytes (count chosen randomly) before the plaintext and 5-10 bytes after the plaintext.
4. Now, have the function choose to encrypt under ECB 1/2 the time, and under CBC the other half (just use random IVs each time for CBC). 
Use rand(2) to decide which to use.

The function should look like:
encryption_oracle(your-input)
=> [MEANINGLESS JIBBER JABBER]

Detect the block cipher mode the function is using each time. You should end up with a piece of code that, pointed at a 
block box that might be encrypting ECB or CBC, tells you which one is happening.
"""


def gen_bytes(bytes_len: int) -> bytes:
    # Generate a key that is key_len bytes long
    key: bytes = randbytes(bytes_len)
    return key


def gen_key(key_len: int) -> bytes:
    key: bytes = urandom(key_len)
    return key


def append(plaintext: bytes) -> bytes:
    # Append 5 to 10 bytes to the pt
    plaintext += gen_bytes(randint(5, 10)) + plaintext + gen_bytes(randint(5, 10))
    return plaintext


def encryption_oracle(pt: bytes) -> tuple[bytes, bytes]:
    ct: bytes = b""
    # Generate random key
    key: bytes = gen_key(16)
    # Pad the plaintext so it is divisible by 16
    pt = append(pt)
    pt = pkcs7(pt, len(pt) + len(pt) % 16)
    # The global key will enable us to decrypt the ct. Contains the index of the block and its AES encryption mode
    enc_modes: dict[int, bytes] = {}

    for i in range(len(pt) // 16):
        enc_algo: int = randint(1, 2)
        if enc_algo == 1:
            # Encrypt in ECB mode
            ct += aes_ecb_enc(key, pt[16*i: 16*(i+1)])
            enc_modes[i] = b"ECB"
        else:
            # Encrypt in CBC mode, and generate random IV
            iv: bytes = gen_bytes(16)
            ct += aes_cbc_enc(key, pt[16*i: 16*(i+1)], iv)
            enc_modes[i] = b"CBC"

    print(enc_modes)
    return ct, key


def detect_enc_mode(ct_block: bytes, key: bytes) -> bytes:
    print(aes_ecb_dec(ct_block, key))
    return b"ECB"


if __name__ == "__main__":
    ciphrat, schlussel = encryption_oracle(b"testing this shit")
    print(ciphrat, schlussel)
