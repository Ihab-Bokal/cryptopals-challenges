from base64 import b64decode

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


if __name__ == "__main__":
    print(ciphered_file)
