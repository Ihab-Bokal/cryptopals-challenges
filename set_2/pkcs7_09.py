def pkcs7(unpadded_pt: bytes, target_length: int) -> bytes:
    length: int = target_length - len(unpadded_pt)
    padding: bytes = bytes([length] * length)
    padded_pt: bytes = unpadded_pt + padding
    return padded_pt


if __name__ == "__main__":
    pt: bytes = b"YELLOW SUBMARINE"
    print(pkcs7(pt, 20))
