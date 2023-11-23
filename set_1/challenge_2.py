#                                                                Fixed XOR
# Write a function that takes two equal-length buffers and produces their XOR combination.
# If your function works properly, then when you feed it the string:
# 1c0111001f010100061a024b53535009181c
# ... after hex decoding, and when XOR'd against:
# 686974207468652062756c6c277320657965
# ... should produce:
# 746865206b696420646f6e277420706c6179
hex_digits = "0123456789abcdef"


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
        bin_d = str(index // 2 ** (3 - i))
        v_list.append(bin_d)
        index -= (2 ** (3 - i)) * int(bin_d)
    return v_list


def binary_to_hexadecimal(bin_v: str):
    result = ""
    for i in range(len(bin_v) // 4):
        temp_list = bin_v[4 * i: 4 * (i + 1)]
        res = 8*int(temp_list[0]) + 4 * int(temp_list[1]) + 2 * int(temp_list[2]) + int(temp_list[3])
        result += hex_digits[res]

    return result


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
    print(binary_to_hexadecimal(result))
    return result


fixed_xor("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965")
print("746865206b696420646f6e277420706c6179")
