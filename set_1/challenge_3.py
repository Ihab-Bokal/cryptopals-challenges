# english_letters = "eariotnslcudpmhgbfywkvxzjq"
#
#
# def frequency(string: str):
#     hex_dict = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "a": 0, "b": 0, "c": 0,
#                 "d": 0, "e": 0, "f": 0}
#     for i in range(len(string)):
#         # Increment the count of the encountered letter
#         hex_dict[string[i]] += 1
#     print(hex_dict)
#     return hex_dict
#
#
# def decipher(ciphertext: str):
#     # This list is going to contain a list of characters
#     result = ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x',
#               'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x',
#               'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x',
#               'x', 'x', 'x', 'x', 'x']
#     cipher_dict = frequency(ciphertext)
#     j = 0
#     maxvalue = max(cipher_dict, key=cipher_dict.get)
#     while maxvalue != 0:
#         for i in range(len(ciphertext)):
#             if ciphertext[i] == 0:
#                 result[i] = english_letters[j]
from set_1.challenge_2 import *


hex_digits = "0123456789abcdef"

x = hexadecimal_to_binary("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
print(x)
















