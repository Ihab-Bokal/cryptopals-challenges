from codecs import decode
from challenge_2 import fixed_xor
hex_digits = "0123456789abcdef"


def frequency(string: str):
    hex_dict = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "a": 0, "b": 0, "c": 0,
                "d": 0, "e": 0, "f": 0}
    for i in range(len(string)):
        # Increment the count of the encountered letter
        hex_dict[string[i]] += 1
    print(hex_dict)


def decipher(string: str):
    for i in range(len(hex_digits)):
        x = decode(fixed_xor("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736", hex_digits[i] * 68), "hex")
        print(x)

"""
from codecs import decode

most_frequent_leters = "eariotnslcudpmhgbfywkvxzjq"
frequent_digits = "3781b269df45abc"

def frequency(string: str):
    hex_dict = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "a": 0, "b": 0, "c": 0,
                "d": 0, "e": 0, "f": 0}
    for i in range(len(string)):
        # Increment the count of the encountered letter
        hex_dict[string[i]] += 1
    print(decode("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736", "hex"))
    print(hex_dict)


def decipher(string: str):
    for 
    return 0


frequency("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
"""
