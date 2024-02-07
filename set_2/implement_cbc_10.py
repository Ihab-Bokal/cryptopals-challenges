from Crypto.Cipher import AES
from set_1.challenge2_solution import xor_buffers
from pkcs7_09 import pkcs7
from set_1.challenge7_solution import aes_ecb_dec
from base64 import b64decode

iv = b"fake 0th ciphertext block"


def aes_ecb_enc(key: bytes, plaintext: bytes) -> bytes:
    # Create an AES object which will encrypt and decrypt the text we provide it with
    cipher_ecb = AES.new(key, AES.MODE_ECB)
    return cipher_ecb.encrypt(plaintext)


def aes_cbc_enc(key: bytes, plaintext: bytes, init_v: bytes) -> bytes:
    ct: bytes = b""
    cipher_to_xor: bytes = init_v
    # Pad the plaintext so it is divisible by 16
    plaintext = pkcs7(plaintext, len(plaintext) + len(plaintext) % 16)
    for i in range(len(plaintext) // 16):
        # XOR with previous ciphered block
        xored_pt: bytes = xor_buffers(cipher_to_xor, plaintext[16*i: 16*(i+1)])
        # Encrypt using the ECB method
        cipher_to_xor = aes_ecb_enc(key, xored_pt)
        ct += aes_ecb_enc(key, xored_pt)
    return ct


# -------------------------- Now write code that will decrypt the file 10.txt --------------------------
with open("10.txt", "r") as file:
    # cf stands for ciphered file
    cf = bytes(file.read(), 'utf-8')


def aes_cbc_dec(key: bytes, ciphertext: bytes, init_v: bytes) -> bytes:
    cipher_to_xor: bytes = init_v[:16]
    pt: bytes = b""
    for i in range(len(ciphertext) // 16):
        # Decrypt the AES ECB block
        decrypted_block: bytes = aes_ecb_dec(key, ciphertext[16 * i: 16 * (i + 1)])
        # XOR with the IV (or previous ciphertext block for subsequent blocks)
        xored_block: bytes = xor_buffers(decrypted_block, cipher_to_xor)
        # Append the result to the plaintext
        pt += xored_block
        # Update the IV for the next iteration
        cipher_to_xor = ciphertext[16 * i: 16 * (i+1)]
    return pt


if __name__ == "__main__":
    enc_key = b"YELLOW SUBMARINE"
    ciphrat: bytes = aes_cbc_enc(enc_key, b"plaintext something to test stuff yeah man, life be hitin real good these days", iv)
    print(aes_cbc_dec(enc_key, ciphrat, iv))
    cipher: bytes = b64decode(cf)
    # print(aes_cbc_dec(enc_key, cipher, bytes([0]*16)))
    # print(bytes([0]*16))
