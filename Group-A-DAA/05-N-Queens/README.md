# Practical 5: N-Queens Problem (Backtracking)

## Objective
Design and implement a Java program to solve the classic $N$-Queens problem using Backtracking. Place $N$ queens on an $N \times N$ chessboard such that no two queens attack each other (no two queens share the same row, column, or diagonal).

---

## Theory
Backtracking incrementally builds candidates to the solutions and abandons each candidate ("backtracks") as soon as it determines that the candidate cannot lead to a valid full solution.

### Safety Checks
Before placing a queen at `board[row][col]`, check:
1. **Left Row**: No queen placed in row on columns $0 \dots col-1$.
2. **Upper-Left Diagonal**: Check cells $(row-i, col-i)$ for $i > 0$.
3. **Lower-Left Diagonal**: Check cells $(row+i, col-i)$ for $i > 0$.

*(Right side does not need checking as queens are placed column by column from left to right).*

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N!)$ in the worst case (searching through permutations).
- **Space Complexity**: $\mathcal{O}(N^2)$ for the chessboard representation, and $\mathcal{O}(N)$ recursion stack depth.

---

## Program Files
- `NQueens.java`: Implementation supporting computation and display of all valid configurations for the given $N$.

---

## How to Compile & Run

```bash
cd Group-A-DAA/05-N-Queens

# Compile
javac NQueens.java

# Run
java NQueens
```

---

## Sample Input & Output
```text
Enter the number of queens (N): 4

Solution 1:
0 0 1 0 
1 0 0 0 
0 0 0 1 
0 1 0 0 

Solution 2:
0 1 0 0 
0 0 0 1 
1 0 0 0 
0 0 1 0 

Total Solutions: 2
```
