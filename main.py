#                                                                Fixed XOR
# Write a function that takes two equal-length buffers and produces their XOR combination.
# If your function works properly, then when you feed it the string:
# 1c0111001f010100061a024b53535009181c
# ... after hex decoding, and when XOR'd against:
# 686974207468652062756c6c277320657965
# ... should produce:
# 746865206b696420646f6e277420706c6179
hex_digits = "0123456789abcdef"


def hex_to_dec(hex_value):
    decimal_value = 0
    for i in range(len(hex_value)):
        # Fixed bug here, I was reading the numbers from left to right, right being coefficients for higher powers
        decimal_value += 16 ** (len(hex_value) - i - 1) * int(hex_digits.index(hex_value[i]))
    return str(decimal_value)


def fixed_xor(string1: str, string2: str):
    result = ""
    len1 = len(string1)
    if len(string1) != len(string2):
        return result

    for i in range(len1):
        if string1[i] == string2[i]:
            result += "0"
        else:
            if int(hex_to_dec(string2[i])) % 2 == 0:
                digit = (int(hex_to_dec(string1[i])) + int(hex_to_dec(string2[i]))) % 16
            else:
                digit = (int(hex_to_dec(string2[i])) - int(hex_to_dec(string1[i]))) % 16
            digit = dec_to_hex(str(digit))
            result += digit

    print(result)
    return result


def dec_to_hex(dec_value):
    # dec_value is a string
    hex_values_list = list()
    decimal_v: int = int(dec_value)
    for i in range(max_power(decimal_v), 0, -1):
        coefficient = decimal_v // (16 ** i)
        hex_values_list.append(coefficient)
        decimal_v -= (16 ** i) * coefficient
    hex_values_list.append(decimal_v)
    return list_to_string(hex_values_list)


def max_power(dec_value):
    i = 0
    while 16 ** i < dec_value:
        i += 1
    return i - 1


def list_to_string(mylist):
    mystring = ""
    for i in range(1, len(mylist) + 1):
        mystring += hex_digits[mylist[i - 1]]
    return mystring


fixed_xor("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965")
print("746865206b696420646f6e277420706c6179")
