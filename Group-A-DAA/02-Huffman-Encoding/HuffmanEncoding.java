
import java.util.*;

// Node class for creating Huffman Tree
class HuffmanNode {

    char ch;                  // Stores character
    int freq;                 // Stores character frequency

    HuffmanNode left, right;  // Left and right child nodes

    // Constructor to initialize character and frequency
    HuffmanNode(char ch, int freq) {
        this.ch = ch;
        this.freq = freq;
    }
}

public class HuffmanEncoding {

    static HuffmanNode root;  // Stores root of Huffman Tree

    // Function to generate and display Huffman Codes
    static void printCodes(HuffmanNode root, String code) {

        // If node is empty, return
        if (root == null)
            return;

        // Check whether current node is a leaf node
        if (root.left == null && root.right == null) {

            // Print character and its binary code
            System.out.println(root.ch + " : " +
                (code.isEmpty() ? "0" : code));

            return;
        }

        // Traverse left side and append 0
        printCodes(root.left, code + "0");

        // Traverse right side and append 1
        printCodes(root.right, code + "1");
    }

    // Function to build Huffman Tree using Greedy Method
    static void buildHuffman(char[] chars, int[] freq) {

        // Create PriorityQueue to store nodes
        // Node with minimum frequency gets highest priority
        PriorityQueue<HuffmanNode> pq =
            new PriorityQueue<>(
                (a, b) -> Integer.compare(a.freq, b.freq)
            );

        // Insert all characters and frequencies into PriorityQueue
        for (int i = 0; i < chars.length; i++) {
            pq.add(new HuffmanNode(chars[i], freq[i]));
        }

        // Repeat until only one node remains
        while (pq.size() > 1) {

            // Remove node having minimum frequency
            HuffmanNode left = pq.poll();

            // Remove second minimum frequency node
            HuffmanNode right = pq.poll();

            // Create new parent node with combined frequency
            HuffmanNode newNode =
                new HuffmanNode('-', left.freq + right.freq);

            // Attach removed nodes as left and right children
            newNode.left = left;
            newNode.right = right;

            // Insert new parent node back into PriorityQueue
            pq.add(newNode);
        }

        // Remaining node becomes root of Huffman Tree
        root = pq.poll();

        System.out.println("\nHuffman Tree Created Successfully!");
    }

    // Main function: execution starts here
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int choice;

        // Arrays to store characters and frequencies
        char[] chars = null;
        int[] freq = null;

        // Checks whether Huffman Tree is created or not
        boolean created = false;

        // Display menu repeatedly until user selects Exit
        do {

            System.out.println("\n--- HUFFMAN ENCODING ---");
            System.out.println("1. Enter Characters and Frequencies");
            System.out.println("2. Generate Huffman Tree");
            System.out.println("3. Display Huffman Codes");
            System.out.println("4. Exit");

            System.out.print("Enter your choice: ");
            choice = sc.nextInt();

            // Execute operation according to user's choice
            switch (choice) {

                case 1:

                    // Accept number of characters
                    System.out.print("Enter number of characters: ");
                    int n = sc.nextInt();

                    // Check whether number is valid
                    if (n <= 0) {
                        System.out.println("Invalid number!");
                        break;
                    }

                    // Create arrays of required size
                    chars = new char[n];
                    freq = new int[n];

                    System.out.println("Enter characters and frequencies:");

                    boolean valid = true;

                    // Accept each character and its frequency
                    for (int i = 0; i < n; i++) {

                        System.out.print("Character " + (i + 1) + ": ");
                        chars[i] = sc.next().charAt(0);

                        System.out.print("Frequency: ");
                        freq[i] = sc.nextInt();

                        // Frequency must be positive
                        if (freq[i] <= 0) {
                            valid = false;
                        }

                        // Check for duplicate characters
                        for (int j = 0; j < i; j++) {
                            if (chars[i] == chars[j]) {
                                valid = false;
                            }
                        }
                    }

                    // Display error if input is invalid
                    if (!valid) {

                        System.out.println(
                            "Invalid input! Characters must be unique "
                            + "and frequencies must be positive."
                        );

                        chars = null;
                        freq = null;
                        created = false;

                    } else {

                        // New input requires a new Huffman Tree
                        created = false;

                        System.out.println("Data entered successfully!");
                    }

                    break;

                case 2:

                    // Check whether characters are entered
                    if (chars == null) {

                        System.out.println(
                            "Please enter characters first!"
                        );

                    } else {

                        // Generate Huffman Tree
                        buildHuffman(chars, freq);

                        created = true;
                    }

                    break;

                case 3:

                    // Check whether tree is generated
                    if (!created) {

                        System.out.println(
                            "Please generate Huffman Tree first!"
                        );

                    } else {

                        // Display generated Huffman Codes
                        System.out.println("\nHuffman Codes:");
                        printCodes(root, "");
                    }

                    break;

                case 4:

                    // Exit the program
                    System.out.println("Exiting Program...");
                    break;

                default:

                    // Handle invalid menu choice
                    System.out.println("Invalid Choice!");
            }

        } while (choice != 4);

        // Close Scanner
        sc.close();
    }
}
