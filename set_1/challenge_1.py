base64_digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def hex_to_dec(hex_value):
    hex_digits = "0123456789abcdef"
    decimal_value = 0
    for i in range(len(hex_value)):
        # Fixed bug here, I was reading the numbers from left to right, right being coefficients for higher powers
        decimal_value += 16 ** (len(hex_value) - i - 1) * int(hex_digits.index(hex_value[i]))
    return str(decimal_value)


def dec_to_base64(dec_value):
    """
    I am going to feed the digits into this list, but it's going to be in a reversed order meaning from coefficient of
    biggest power to that of the smallest
    """
    base64_values_queue = list()
    decimal_v: int = int(dec_value)
    for i in range(max_power(decimal_v), 0, -1):
        coefficient = decimal_v // (64 ** i)
        base64_values_queue.append(coefficient)
        decimal_v -= (64 ** i) * coefficient
    base64_values_queue.append(decimal_v)
    return list_to_string(base64_values_queue)


def max_power(dec_value):
    i = 0
    while 64 ** i < dec_value:
        i += 1
    return i-1


def list_to_string(mylist):
    mystring = ""
    for i in range(1, len(mylist)+1):
        mystring += base64_digits[mylist[i-1]]
    return mystring


print(dec_to_base64(hex_to_dec("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")))
print("SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t")
