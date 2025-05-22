from huffman import decode
import pickle


if __name__ == "__main__":
    with open("output_compressed.txt", "r") as f:
        encoded = f.read()

    with open("output_tree.pkl", "rb") as f:
        tree = pickle.load(f)

    decoded = decode(encoded, tree)

    with open("output_decompressed.txt", "w", encoding="utf-8") as f:
        f.write(decoded)
