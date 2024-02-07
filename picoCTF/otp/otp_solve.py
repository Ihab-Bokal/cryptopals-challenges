from pwn import connect

KEY_LEN = 50_000
hex_key: str = "3035415c7864347b715c7863305c7839325c7831375c7861373c5c7863355c78"
hex_cipher: str = "551257106e1a52095f654f510a6b4954026c1e0304394100043a1c5654505b6b"


def get_key():
    conn = connect("mercury.picoctf.net", 36449)
    key_location: int = 32
    key: str
    while key_location < 50_000:
        if KEY_LEN - key_location > 1_000:
            # Send 1 000 bytes to the server
            print("[+] - sending 1 000 bytes")
            conn.send(b"a" * 1_000 + b'\r\n')
            print("[+] - receiving ciphered 1 000 bytes")
            conn.recvuntil(b"What data would you like to encrypt?")
            key_location += 1_000
        else:
            remaining_pad: int = key_location - KEY_LEN + 1_000
            print(f"[+] - sending last {remaining_pad} bytes")
            conn.send(bytes([0] * remaining_pad) + b'\r\n')
            print(f"[+] - receiving last {remaining_pad} bytes of the key file")
            conn.recvuntil(b"What data would you like to encrypt?")

            print(f"[+] - sending 32 bytes to retrieve the key")
            # I won't have to re-XOR
            conn.send(bytes([0] * 32) + b'\r\n')
            print(f"[+] - receiving the key")
            key = conn.recvuntil(b"What data would you like to encrypt?")
            print(key)
            break

    conn.close()


def break_cipher() -> str:
    byte_key: bytes = bytes.fromhex(hex_key)
    byte_cipher: bytes = bytes.fromhex(hex_cipher)
    flag_list: list[chr] = list(map(lambda c, k: chr(c ^ k), byte_cipher, byte_key))
    return "".join(flag_list)


if __name__ == "__main__":
    # get_key() ===> Gets me the key : 3035415c7864347b715c7863305c7839325c7831375c7861373c5c7863355c78
    print(break_cipher())
