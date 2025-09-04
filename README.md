# Huffencypher

🔐 Huffman Cipher Compression & Decompression

This project demonstrates the Huffman Coding algorithm for lossless data compression and decompression.
Huffman Coding assigns shorter binary codes to frequently occurring characters and longer codes to less frequent ones, optimizing storage space without losing any data.
It serves as a beginner-friendly introduction to data compression techniques using Python.


---

📌 Problem Statement

To create a program that:

Compresses text into a binary representation using Huffman Coding.

Stores the generated Huffman code dictionary for decoding.

Decompresses the binary data back into the original text without any loss.



---

📊 Dataset / Input Overview

Source: User-provided text or file.

Rows / Characters: Varies depending on input size.

Features:

Raw Text Input

Character Frequency

Huffman Binary Codes

Compressed Output Size




---

⚙ Tools & Technologies

Language: Python 3

Libraries:

heapq (priority queue for building Huffman Tree)

collections.Counter (counting character frequency)

pickle (optional, for saving and loading compressed data)




---

🧮 Algorithm Steps

1. Read Input Text


2. Count Character Frequency


3. Build Huffman Tree


4. Generate Huffman Codes


5. Encode Text into Binary


6. Store Huffman Codes for Decoding


7. Decode Binary Data to Original Text




---

📂 Project Structure

📁 HuffmanCipher
│── 📜 huffman_compress.py   # Compression logic
│── 📜 huffman_decompress.py # Decompression logic
│── 📜 utils.py               # Helper functions
│── 📜 README.md              # Project documentation
│── 📄 sample.txt             # Example input file
│── 📄 compressed.bin         # Example compressed output
│── 📄 codes.pkl               # Huffman codes dictionary


---

🖥 Example Usage

Compression

python huffman_compress.py sample.txt

Decompression

python huffman_decompress.py compressed.bin codes.pkl


---

📈 Results

Metric	Original Text	Compressed Binary

Size (bytes)	1200	650
Compression Ratio	-	45.8% smaller
Data Loss	None	None



---

📜 License

This project is licensed under the MIT License.




If you want, I can now also design this README with emojis, icons, and color highlights like your Titanic example so it visually matches perfectly.

Do you want me to make that styled version next?
