# Huffman Compressor

A simple and efficient Python implementation of the **Huffman Coding** algorithm for **lossless text compression**. This project allows you to compress and decompress text files using Huffman coding, making it an educational and practical resource for anyone learning data compression algorithms.

![Huffman Tree Example](https://upload.wikimedia.org/wikipedia/commons/5/5a/Huffman_tree_Visualisation.svg)

---

## 🔍 Features

- 🔠 Compress any text file using Huffman Coding
- 🗃️ Save compressed output and Huffman tree structure
- 🔄 Decompress files back to their original text
- 📦 Lightweight and easy to understand
- 📚 Well-commented and beginner-friendly Python code

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone git@github.com:yuzaiakira/huffman-compressor.git
cd huffman-compressor
```

### 2. Install Python (if not installed)

Make sure you have **Python 3.6+** installed.

### 3. Prepare Input File

Put your text into a file named `input.txt`.

### 4. Run the Compressor

```bash
python compress.py
```

This will generate:

* `output_compressed.txt` — The encoded binary string.
* `output_tree.pkl` — The serialized Huffman tree for decoding.

### 5. Run the Decompressor

```bash
python decompress.py
```

This will generate:

* `output_decompressed.txt` — The recovered original text.

---

## 🧠 How It Works

Huffman coding is a greedy algorithm used for **lossless data compression**. It works by:

1. Counting the frequency of each character in the input.
2. Building a binary tree based on frequencies.
3. Assigning shorter binary codes to more frequent characters.
4. Encoding and decoding using this tree.

This project uses Python’s built-in:

* `collections.Counter` for frequency analysis
* `heapq` for efficient tree construction
* `pickle` to serialize the Huffman tree

---

## 📁 File Structure

```
.
├── compress.py              # Main compressor script
├── decompress.py            # Main decompressor script
├── input.txt                # Your source text file
├── output_compressed.txt    # Encoded binary string
├── output_tree.pkl          # Serialized Huffman tree
├── output_decompressed.txt  # Decoded text output
```

---

## 📸 Example

**input.txt**

```
data compression is fun
```

**output\_compressed.txt**

```
10110011010101... (binary)
```

**output\_decompressed.txt**

```
data compression is fun
```

---

## 🔐 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 🙋‍♂️ Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📈 SEO Keywords

Huffman Coding, Text Compression in Python, Huffman Algorithm, Lossless Compression, Python Huffman Tree, File Compression Script, Python Algorithms, Data Compression, Huffman Encoding and Decoding, Python Projects for Beginners



