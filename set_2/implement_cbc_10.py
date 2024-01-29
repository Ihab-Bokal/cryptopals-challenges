from Crypto.Cipher import AES
from set_1.challenge2_solution import xor_buffers
from pkcs7_09 import pkcs7


def aes_ecb_enc(key: bytes, plaintext: bytes) -> bytes:
    # Create an AES object which will encrypt and decrypt the text we provide it with
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(plaintext)


def aes_cbc_enc(key: bytes, plaintext: bytes) -> bytes:
    ct = b""
    cipher_to_xor = iv
    # We pad the plaintext
    return ct


iv = "fake 0th ciphertext block"


if __name__ == "__main__":
    print(aes_ecb_enc(b"YELLOW SUBMARINE", pkcs7(b"plaintext", 16)))

