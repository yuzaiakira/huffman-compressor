import heapq
from collections import Counter, namedtuple


Node = namedtuple("Node", ["char", "freq", "left", "right"])

def build_tree(text):
    frequency = Counter(text)
    heap = []
    count = 0
    for char, freq in frequency.items():
        heap.append([freq, count, Node(char, freq, None, None)])
        count += 1
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)[2]
        right = heapq.heappop(heap)[2]
        merged = Node(None, left.freq + right.freq, left, right)
        heapq.heappush(heap, [merged.freq, count, merged])
        count += 1
    return heap[0][2]


def build_codes(node, prefix="", codebook={}):
    if node.char is not None:
        codebook[node.char] = prefix
    else:
        build_codes(node.left, prefix + "0", codebook)
        build_codes(node.right, prefix + "1", codebook)
    return codebook


def encode(text, codebook):
    return "".join(codebook[char] for char in text)


def decode(encoded, node):
    decoded = ""
    current = node
    for bit in encoded:
        current = current.left if bit == "0" else current.right
        if current.char is not None:
            decoded += current.char
            current = node
    return decoded
