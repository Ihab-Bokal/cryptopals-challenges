from Crypto.Cipher import AES
from set_1.challenge2_solution import xor_buffers
from pkcs7_09 import pkcs7

iv = b"fake 0th ciphertext block"


def aes_ecb_enc(key: bytes, plaintext: bytes) -> bytes:
    # Create an AES object which will encrypt and decrypt the text we provide it with
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(plaintext)


def aes_cbc_enc(key: bytes, plaintext: bytes) -> bytes:
    ct: bytes = b""
    cipher_to_xor: bytes = iv
    xored_pt: bytes
    # Pad the plaintext so it is divisible by 16
    plaintext = pkcs7(plaintext, len(plaintext) + len(plaintext) % 16)
    for i in range(len(plaintext) // 16):
        # XOR with previous ciphered block
        xored_pt = xor_buffers(cipher_to_xor, plaintext[16*i: 16*(i+1)])
        # Encrypt using the ECB method
        cipher_to_xor += aes_ecb_enc(key, xored_pt)
        ct += aes_ecb_enc(key, xored_pt)
    return ct


if __name__ == "__main__":
    enc_key = b"YELLOW SUBMARINE"
    print(aes_cbc_enc(enc_key, b"plaintext something to test shit yeah man, lkife be hhittin real good these days"))
