from challenge2_solution import xor_buffers
"""
The challenge says to encrypt my SIG file, SIG files contain signatures to identify the mail's sender. 
SIG files are characteristic files of Outlook
"""

plaintext = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
email = b"bokalihab@gmail.com"
password = b"password123_will_never_be_my_passwd"


def generate_key(length: int, key: bytes) -> bytes:
    ice = key
    key: bytes
    root_key = key * (length//3)
    key = root_key + ice[:length % 3]
    return key


def ice_encryption(pt: bytes) -> str:
    # pt here stands for plaintext
    length = len(pt)
    key = generate_key(length, b"ICE")
    ciphertext = xor_buffers(key, pt)
    return ciphertext.hex()


if __name__ == "__main__":
    # I passed this test, the encryption is done successfully
    # print(ice_encryption(plaintext) == "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f")
    print(ice_encryption(email))
    print(ice_encryption(password))

