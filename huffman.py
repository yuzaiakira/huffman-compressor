import heapq
from collections import Counter, namedtuple


class Node(namedtuple("Node", ["char", "freq", "left", "right"])):
    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(text):
    frequency = Counter(text)
    heap = [Node(char, freq, None, None) for char, freq in frequency.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq, left, right)
        heapq.heappush(heap, merged)
    return heap[0]


def build_codes(node, prefix="", code_map=None):
    if code_map is None:
        code_map = {}
    if node.char is not None:
        code_map[node.char] = prefix
    else:
        build_codes(node.left, prefix + "0", code_map)
        build_codes(node.right, prefix + "1", code_map)
    return code_map


def huffman_encode(text):
    tree = build_huffman_tree(text)
    codes = build_codes(tree)
    encoded_text = ''.join(codes[char] for char in text)
    return encoded_text, tree


def huffman_decode(encoded_text, tree):
    decoded_text = ""
    node = tree
    for bit in encoded_text:
        node = node.left if bit == '0' else node.right
        if node.char:
            decoded_text += node.char
            node = tree
    return decoded_text
