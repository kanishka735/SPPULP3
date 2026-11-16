# Practical 2: Huffman Encoding (Greedy Strategy)

## Objective
Write a Java program to implement Huffman Encoding using the greedy strategy. Build a Huffman tree from given characters and their frequencies, and generate optimal prefix-free binary codes for data compression.

---

## Theory
Huffman coding is a lossless data compression algorithm. The idea is to assign variable-length prefix codes to input characters:
- Characters with higher frequencies receive shorter binary codes.
- Characters with lower frequencies receive longer binary codes.
- No code is a prefix of any other code (prefix rule), ensuring unambiguous decoding.

A **Min-Priority Queue** (Min-Heap) is used to repeatedly combine the two nodes with the lowest frequencies into a new parent node whose frequency is the sum of both children.

---

## Algorithm Steps
1. Count the frequency of each unique character.
2. Insert all leaf nodes into a Min-Priority Queue.
3. While the queue has more than 1 node:
   - Extract the two nodes with the smallest frequencies ($L$ and $R$).
   - Create a parent internal node with frequency $= \text{freq}(L) + \text{freq}(R)$.
   - Assign $L$ as the left child and $R$ as the right child.
   - Insert the parent node back into the priority queue.
4. The remaining node in the queue is the root of the Huffman Tree.
5. Traverse the tree from root to leaves (assign `0` for left edge, `1` for right edge) to produce the codes.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n \log n)$, where $n$ is the number of distinct characters (due to heap operations).
- **Space Complexity**: $\mathcal{O}(n)$ to store the tree and priority queue.

---

## Program Files
- `02_huffman.java`: Original submission file.
- `HuffmanEncoding.java`: Ready-to-compile file matching the public class `HuffmanEncoding`.

---

## How to Compile & Run

```bash
cd Group-A-DAA/02-Huffman-Encoding

# Compile
javac HuffmanEncoding.java

# Run
java HuffmanEncoding
```

---

## Sample Input & Output
```text
Enter number of characters: 6
Enter character: a
Enter frequency of a: 5
Enter character: b
Enter frequency of b: 9
Enter character: c
Enter frequency of c: 12
Enter character: d
Enter frequency of d: 13
Enter character: e
Enter frequency of e: 16
Enter character: f
Enter frequency of f: 45

Huffman Codes:
f : 0
c : 100
d : 101
a : 1100
b : 1101
e : 111
```
