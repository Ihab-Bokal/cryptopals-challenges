from codecs import decode

buffer1 = decode(b"1c0111001f010100061a024b53535009181c", "hex_codec")
buffer2 = decode(b"686974207468652062756c6c277320657965", "hex_codec")


def xor_buffers(buf1: bytes, buf2: bytes) -> bytes:
    result = [x ^ y for x, y in zip(buf1, buf2)]
    return bytes(result)


xor_buffers(buffer1, buffer2).hex()
