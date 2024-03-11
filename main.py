from Crypto.Util.number import *
from pwn import xor


# def decode_base64_file(input_file, output_file):
#     try:
#         # Read the content of the input file
#         with open(input_file, 'rb') as file:
#             encoded_data = file.read()
#
#         # Decode the content from base64 to bytes
#         decoded_data = base64.b64decode(encoded_data)
#
#         # Write the decoded content to the output file
#         with open(output_file, 'wb') as file:
#             file.write(decoded_data)
#
#         print(f"Decoding successful. Decoded data written to {output_file}")
#
#     except FileNotFoundError:
#         print(f"Error: File '{input_file}' not found.")
#     except Exception as e:
#         print(f"Error: {e}")


if __name__ == "__main__":
    # Replace 'input_file.txt' and 'output_file.txt' with your actual file names
    key1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
    key2 = bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
    key2 = xor(key2, key1)
    key3 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
    key3 = xor(key3, key2)
    flag = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

    flag = xor(key2, key1, key3, flag)
    print(flag)

    


