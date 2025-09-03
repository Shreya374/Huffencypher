import heapq
from collections import defaultdict
import tkinter as tk
from tkinter import scrolledtext

# Huffman Node and related functions (as corrected previously)
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    freq = defaultdict(int)
    for char in text:
        freq[char] += 1

    heap = [HuffmanNode(c, f) for c, f in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def generate_codes(node, code="", mapping=None):
    if mapping is None:
        mapping = {}
    if node is None:
        return mapping
    if node.char is not None:
        mapping[node.char] = code
    generate_codes(node.left, code + "0", mapping)
    generate_codes(node.right, code + "1", mapping)
    return mapping

def huffman_compress(text):
    root = build_huffman_tree(text)
    huffman_codes = generate_codes(root)
    encoded_text = ''.join(huffman_codes[char] for char in text)
    return encoded_text, huffman_codes

def huffman_decompress(encoded_text, codes):
    reverse_codes = {v: k for k, v in codes.items()}
    current_code = ""
    decoded_text = ""
    for bit in encoded_text:
        current_code += bit
        if current_code in reverse_codes:
            decoded_text += reverse_codes[current_code]
            current_code = ""
    return decoded_text

def xor_encrypt_bytes(data_bytes, key):
    return bytes([b ^ key for b in data_bytes])

def binary_to_bytes(bin_str):
    return bytes(int(bin_str[i:i+8], 2) for i in range(0, len(bin_str), 8))

def bytes_to_binary(byte_data):
    return ''.join(f'{b:08b}' for b in byte_data)

# Tkinter GUI
def process_text():
    text = text_input.get("1.0", tk.END).strip()
    if not text:
        result_output.config(state='normal')
        result_output.delete("1.0", tk.END)
        result_output.insert(tk.END, "Please enter some text.\n")
        result_output.config(state='disabled')
        return

    compressed_binary, codes = huffman_compress(text)
    padded_binary = compressed_binary.ljust((len(compressed_binary) + 7) // 8 * 8, '0')
    byte_data = binary_to_bytes(padded_binary)
    encrypted_bytes = xor_encrypt_bytes(byte_data, 5)
    decrypted_bytes = xor_encrypt_bytes(encrypted_bytes, 5)
    decrypted_binary = bytes_to_binary(decrypted_bytes)[:len(compressed_binary)]
    decompressed_text = huffman_decompress(decrypted_binary, codes)

    result_output.config(state='normal')
    result_output.delete("1.0", tk.END)
    result_output.insert(tk.END, f"Original: {text}\n\n")
    result_output.insert(tk.END, f"Compressed (binary): {compressed_binary}\n\n")
    result_output.insert(tk.END, f"Encrypted (bytes): {encrypted_bytes}\n\n")
    result_output.insert(tk.END, f"Decrypted Binary: {decrypted_binary}\n\n")
    result_output.insert(tk.END, f"Decompressed Text: {decompressed_text}\n")
    result_output.config(state='disabled')

root = tk.Tk()
root.title("Huffman Compression with XOR Encryption")

tk.Label(root, text="Enter text below:").pack(anchor='w')
text_input = scrolledtext.ScrolledText(root, width=50, height=5)
text_input.pack(padx=10, pady=5)

process_button = tk.Button(root, text="Compress & Encrypt", command=process_text)
process_button.pack(pady=5)

tk.Label(root, text="Results:").pack(anchor='w', padx=10)
result_output = scrolledtext.ScrolledText(root, width=70, height=15, state='disabled')
result_output.pack(padx=10, pady=5)

root.mainloop()            