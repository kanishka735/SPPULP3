# Practical 1: Fibonacci Numbers (Non-Recursive and Recursive)

## Objective
Write a Java program to calculate Fibonacci numbers using both non-recursive (iterative) and recursive algorithms. Analyze and compare their time and space complexities.

---

## Theory & Mathematical Formulation
The Fibonacci sequence is defined by the recurrence relation:
$$F_0 = 0, \quad F_1 = 1, \quad F_n = F_{n-1} + F_{n-2} \quad \text{for } n \ge 2$$

- **Iterative Approach**: Uses dynamic programming / bottom-up loop to maintain the two most recent values.
- **Recursive Approach**: Directly computes $F(n) = F(n-1) + F(n-2)$, forming a binary recursion tree.

---

## Complexity Analysis

| Method | Time Complexity | Auxiliary Space Complexity | Recursion Depth |
| :--- | :--- | :--- | :--- |
| **Iterative (Non-Recursive)** | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | None |
| **Recursive** | $\mathcal{O}(2^n)$ (Exponential) | $\mathcal{O}(n)$ | $n$ |

---

## Program Files
- `01_fibo.java`: Original submission file.
- `Main.java`: Ready-to-compile file matching the public class name `Main`.

---

## How to Compile & Run

### Using Standard Java Compiler
```bash
# Navigate to this directory
cd Group-A-DAA/01-Fibonacci

# Compile
javac Main.java

# Run
java Main
```

*(Note: If compiling `01_fibo.java` directly, compile with `javac 01_fibo.java` if `Main.java` is present or rename class to match file name).*

---

## Sample Input & Output
```text
===== FIBONACCI MENU =====
1. Non-Recursive Fibonacci
2. Recursive Fibonacci
3. Exit
Enter your choice: 1
Enter number of terms (0-93): 8
Fibonacci Series:
0 1 1 2 3 5 8 13 
Execution Time: 0.003200 ms
Time Complexity: O(n)
Auxiliary Space Complexity: O(1)
```
