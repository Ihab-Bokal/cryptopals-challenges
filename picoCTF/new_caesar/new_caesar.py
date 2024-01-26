import string

LOWERCASE_OFFSET = ord("a")
# lowercase letters from a to p
ALPHABET = string.ascii_lowercase[:16]


def b16_encode(plain: str) -> str:
	encoded = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))
		encoded += ALPHABET[int(binary[:4], 2)]
		encoded += ALPHABET[int(binary[4:], 2)]
	return encoded


def shift(c: chr, k: chr):
	# Convert to the index of the ascii_lowercase string
	t1: int = ord(c) - LOWERCASE_OFFSET
	t2: int = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]


flag = "mlnklfnknljflfjljnjijjmmjkmljnjhmhjgjnjjjmmkjjmijhmkjhjpmkmkmljkjijnjpmhmjjgjj"
key = "a"

if __name__ == "__main__":
	# Check that all the key's characters are between a and p
	assert all([k in ALPHABET for k in key])
	# Check that the key is of length 1
	assert len(key) == 1

	# Encode the flag in base 16
	b16 = b16_encode(flag)
	# variable for the encrypted flag
	enc = ""
	for potential_key in ALPHABET[:16]:
		print("[+] - double ciphered flag for " + potential_key + " :")
		for i, c in enumerate(b16):
			# Since the key length is 1, then this stmt is equiv
			# enc += shift(c, key)
			enc += shift(c, potential_key[i % len(potential_key)])
		print(enc)
		enc = ""
