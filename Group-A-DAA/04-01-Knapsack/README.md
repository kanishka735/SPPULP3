# Practical 4: 0/1 Knapsack Problem (Dynamic Programming & Branch and Bound)

## Objective
Write Java programs to solve the 0/1 Knapsack problem using two distinct paradigms:
1. **Dynamic Programming (DP)**: Bottom-up tabulation approach.
2. **Branch and Bound (LCBB / FIFO BB)**: State-space tree exploration with upper bound calculation and pruning.

---

## Theory & Comparison

| Aspect | Dynamic Programming (`Knapsack01.java`) | Branch and Bound (`KnapsackBB.java`) |
| :--- | :--- | :--- |
| **Strategy** | Tabulation of overlapping subproblems | State Space Tree with pruning |
| **Recurrence / Bound** | $DP[i][w] = \max(DP[i-1][w], p_i + DP[i-1][w-w_i])$ | Fractional Knapsack upper bound |
| **Item Fractionality** | 0 or 1 (cannot take fractions) | 0 or 1 (cannot take fractions) |
| **Time Complexity** | $\mathcal{O}(n \cdot W)$ (Pseudo-polynomial) | $\mathcal{O}(2^n)$ worst-case, much faster on average with pruning |
| **Space Complexity** | $\mathcal{O}(n \cdot W)$ 2D DP table | $\mathcal{O}(2^n)$ max queue/tree nodes |

---

## Program Files
- `Knapsack01.java`: Solves 0/1 Knapsack using Dynamic Programming with full DP table visualization and backtrack tracking of chosen items.
- `KnapsackBB.java`: Solves 0/1 Knapsack using Branch and Bound with upper-bound estimation and pruning.

---

## How to Compile & Run

### 1. Dynamic Programming
```bash
cd Group-A-DAA/04-01-Knapsack

# Compile
javac Knapsack01.java

# Run
java Knapsack01
```

### 2. Branch and Bound
```bash
cd Group-A-DAA/04-01-Knapsack

# Compile
javac KnapsackBB.java

# Run
java KnapsackBB
```

---

## Sample Input & Output (Dynamic Programming)
```text
Enter number of items: 4
Enter weights of items:
2 3 4 5
Enter profits of items:
3 4 5 6
Enter knapsack capacity: 5

DP Table:
0 0 0 0 0 0 
0 0 3 3 3 3 
0 0 3 4 4 7 
0 0 3 4 5 7 
0 0 3 4 5 7 

Maximum Profit: 7
Selected items (1-based index): 2 1
```
