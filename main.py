import pickle
from huffman import *

def save_to_file(encoded_text, tree, filename_prefix):
    with open(f"{filename_prefix}_compressed.txt", "w") as f:
        f.write(encoded_text)
    with open(f"{filename_prefix}_tree.pkl", "wb") as f:
        pickle.dump(tree, f)


def compress_file(input_file, filename_prefix="output"):
    with open(input_file, "r") as f:
        text = f.read()

    encoded, tree = huffman_encode(text)
    save_to_file(encoded, tree, filename_prefix)

    print("Compressed successfully.")
    return encoded, tree


def decompress_file(filename_prefix="output"):
    with open(f"{filename_prefix}_compressed.txt", "r") as f:
        encoded_text = f.read()
    with open(f"{filename_prefix}_tree.pkl", "rb") as f:
        tree = pickle.load(f)

    decoded = huffman_decode(encoded_text, tree)
    with open(f"{filename_prefix}_decoded.txt", "w") as f:
        f.write(decoded)

    print("Decompressed successfully.")
    return decoded


if __name__ == "__main__":
    input_file = "input.txt"  
    encoded, tree = compress_file(input_file, "output")
    decoded = decompress_file("output")
