from Crypto.Cipher import AES
from challenge7 import ciphered_file


def aes_ecb_dec(key: bytes, ciphertext: bytes) -> bytes:
    # Create an AES object which will encrypt and decrypt the text we provide it with
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(ciphertext)


if __name__ == "__main__":
    enc_key = b"YELLOW SUBMARINE"
    pt = aes_ecb_dec(enc_key, ciphered_file)
    print(pt)


"""
The solution was in using predefined classes (AES) and methods / functions and not re-inventing the cycle
"""