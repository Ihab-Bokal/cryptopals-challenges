if __name__ == "__main__":
    numbersList: list[int] = [16, 9, 3, 15, 3, 20, 6, 27, 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14, 29]
    flag: str = ""

    for chr_ord in numbersList:
        flag += chr(chr_ord + 96)

    print(flag)
