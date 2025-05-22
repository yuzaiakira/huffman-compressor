from huffman import build_tree, build_codes, encode
import pickle


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f:
        text = f.read()

    tree = build_tree(text)
    codebook = build_codes(tree)
    encoded = encode(text, codebook)

    with open("output_compressed.txt", "w") as f:
        f.write(encoded)

    with open("output_tree.pkl", "wb") as f:
        pickle.dump(tree, f)
