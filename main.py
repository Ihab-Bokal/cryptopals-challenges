from codecs import decode
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
    return binary_to_hexadecimal(result)


def decipher(string: str):
    for i in range(len(hex_digits)):
        x = decode(fixed_xor("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736", hex_digits[i] * 68), "hex")
        print(str(x))


decipher("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
