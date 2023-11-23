#                                                                Fixed XOR
# Write a function that takes two equal-length buffers and produces their XOR combination.
# If your function works properly, then when you feed it the string:
# 1c0111001f010100061a024b53535009181c
# ... after hex decoding, and when XOR'd against:
# 686974207468652062756c6c277320657965
# ... should produce:
# 746865206b696420646f6e277420706c6179
hex_digits = "0123456789abcdef"
binary_digits = "01"

"""
def hex_to_dec(hex_value):
    decimal_value = 0
    for i in range(len(hex_value)):
        # Fixed bug here, I was reading the numbers from left to right, right being coefficients for higher powers
        decimal_value += 16 ** (len(hex_value) - i - 1) * int(hex_digits.index(hex_value[i]))
    return str(decimal_value)


def binary_to_dec(binary_value):
    decimal_value = 0
    for i in range(len(binary_value)):
        # Fixed bug here, I was reading the numbers from left to right, right being coefficients for higher powers
        decimal_value += 2 ** (len(binary_value) - i - 1) * int(binary_digits.index(binary_value[i]))
    return str(decimal_value)


def dec_to_hex(dec_value):
    # dec_value is a string
    hex_values_list = list()
    decimal_v: int = int(dec_value)
    for i in range(max_power(decimal_v, 16), 0, -1):
        coefficient = decimal_v // (16 ** i)
        hex_values_list.append(coefficient)
        decimal_v -= (16 ** i) * coefficient
    hex_values_list.append(decimal_v)
    return list_to_string(hex_values_list)


def max_power(dec_value, base: int):
    i = 0
    while base ** i < dec_value:
        i += 1
    return i-1


def dec_to_bin(dec_value):
    binary_values_list = list()
    decimal_v: int = int(dec_value)
    for i in range(max_power(decimal_v, 2), 0, -1):
        coefficient = decimal_v // (2 ** i)
        binary_values_list.append(coefficient)
        decimal_v -= (2 ** i) * coefficient
    binary_values_list.append(decimal_v)
    return list_to_string(binary_values_list)


def list_to_string(mylist):
    mystring = ""
    for i in range(1, len(mylist)+1):
        mystring += hex_digits[mylist[i-1]]
    return mystring


def fixed_xor(string1: str, string2: str):
    result = ""
    len1 = len(string1)
    if len(string1) != len(string2):
        return result

    for i in range(len1):
        if string1[i] == string2[i]:
            result += "0"
        else:
            digit = (hex_to_dec(string1) + hex_to_dec(string2)) % 2
            digit = dec_to_hex(str(digit))
            result += digit
    return result


fixed_xor("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965")
print("746865206b696420646f6e277420706c6179")
"""

"""
1. Transform hex to binary
2. XOR the binaries
3. Transform the binary back to hex
"""


def hexadecimal_to_binary(hex_v: str):
    result: str = ""
    for i in range(len(hex_v)):
        result += "".join(hex_digit_to_binary(hex_v[i]))
    return result


def hex_digit_to_binary(hex_d: str):
    index = hex_digits.index(hex_d)
    bin_d: str = ""
    v_list = list()
    for i in range(4):
        bin_d = str(index // 2 ** (3-i))
        v_list.append(bin_d)
        index -= (2 ** (3-i)) * int(bin_d)
    return v_list


def fixed_xor(hex1: str, hex2: str):
    binary1 = hexadecimal_to_binary(hex1)
    binary2 = hexadecimal_to_binary(hex2)
    result = ""
    if len(hex1) != len(hex2):
        return ""
    else:
        for i in range(len(binary1)):
            res = (int(binary2[i]) + int(binary1[i])) % 2
            result += str(res)
    print(result)
    return result


print(fixed_xor("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965"))
print(hexadecimal_to_binary("746865206b696420646f6e277420706c6179"))
