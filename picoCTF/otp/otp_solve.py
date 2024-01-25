from pwn import connect
from set_1 import challenge2_solution


if __name__ == "__main__":
    # conn = connect("mercury.picoctf.net", 36449)
    # print(conn.recvuntil("What data would you like to encrypt?"))
    #
    # # Flag is 32 bytes long
    # remaining_bytes: int = 50_000 - 32
    #
    # while remaining_bytes >= 1_000:
    #     print("[+] - sending 1_000 bytes")
    #     conn.send(b'a' * 1_000 + b"\r\n")
    #     remaining_bytes -= 1_000
    #     conn.recvuntil("What data would you like to encrypt?")
    #
    # print(f'sending {remaining_bytes} bytes')
    # conn.send(b'a' * remaining_bytes + b"\r\n")
    # print(conn.recvuntil("What data would you like to encrypt?"))
    # print("--------------------------------- + [+] + ---------------------------------")
    # print("[+] - The key offset is now at position 0")
    # print(f"Sending 'a' * 32 ...")
    # conn.send(b'b' * 32 + b"\r\n")
    # print("[+} - Ciphered a * 32 : ")
    # print(conn.recvuntil("What data would you like to encrypt?"))
    #
    # conn.close()
    # print("Done")
    print("[+] - Key is :")
    c1c2 = challenge2_solution.xor_buffers(b"004506423e1a03530b3e1a52503e1a01063e1a00033e1a01563e1a0700530c3e", b"551257106e1a52095f654f510a6b4954026c1e0304394100043a1c5654505b6b")

    print(b"flag : " + challenge2_solution.xor_buffers(b"b" * 32, c1c2))
