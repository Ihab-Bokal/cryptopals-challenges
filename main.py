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
    """cipherflag = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")
    keylen = len(cipherflag)

    for i in range(127):
        flag = xor(cipherflag, bytes([i])*keylen)
        if flag.count(b"crypto") != 0:
            print(flag, " : ", i)"""

    """ Repeating key XOR
    
    cipherflag: bytes = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
    flaglen = len(cipherflag)
    flagFormat = b"crypto{"

    print(b"key is : ", xor(flagFormat, cipherflag))
    key: bytes = b"myXORkey"
    keylen: int = len(key)
    key = key * (flaglen // keylen)
    print(len(key), flaglen)
    print(b"flag is : ", xor(cipherflag, key))"""
