import base64


def decode_base64_file(input_file, output_file):
    try:
        # Read the content of the input file
        with open(input_file, 'rb') as file:
            encoded_data = file.read()

        # Decode the content from base64 to bytes
        decoded_data = base64.b64decode(encoded_data)

        # Write the decoded content to the output file
        with open(output_file, 'wb') as file:
            file.write(decoded_data)

        print(f"Decoding successful. Decoded data written to {output_file}")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    # Replace 'input_file.txt' and 'output_file.txt' with your actual file names
    decode_base64_file('set_1/7.txt', 'set_1/7_decoded.txt')
