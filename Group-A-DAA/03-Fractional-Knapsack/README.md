# Practical 3: Fractional Knapsack Problem (Greedy Strategy)

## Objective
Write a Java program to solve the Fractional Knapsack Problem using the Greedy Method. Maximize the total profit within a specified weight capacity by taking complete items or fractional parts.

---

## Theory
In the Fractional Knapsack Problem, items can be broken into smaller fractions:
- For each item $i$, calculate its profit-to-weight ratio: $r_i = \frac{p_i}{w_i}$.
- Sort all items in descending order of $r_i$.
- Greedily pick items with the highest ratio:
  - If the item fits entirely ($w_i \le W$), take 100% of it.
  - If the item exceeds remaining capacity $W$, take a fraction $\frac{W}{w_i}$ to completely fill the knapsack and terminate.

Unlike 0/1 Knapsack, the greedy strategy is mathematically guaranteed to yield the optimal solution for Fractional Knapsack.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n \log n)$ due to sorting items by ratio. The linear scan takes $\mathcal{O}(n)$.
- **Space Complexity**: $\mathcal{O}(1)$ auxiliary space (or $\mathcal{O}(n)$ to store item structures).

---

## Program Files
- `03_fractional_Knapsack.java`: Original submission file.
- `FractionalKnapsack.java`: Ready-to-compile file matching the public class `FractionalKnapsack`.

---

## How to Compile & Run

```bash
cd Group-A-DAA/03-Fractional-Knapsack

# Compile
javac FractionalKnapsack.java

# Run
java FractionalKnapsack
```

---

## Sample Input & Output
```text
Enter number of items: 3
Enter weight for item 1: 10
Enter profit for item 1: 60
Enter weight for item 2: 20
Enter profit for item 2: 100
Enter weight for item 3: 30
Enter profit for item 3: 120
Enter knapsack capacity: 50

Selected Items:
Item with weight 10 and profit 60 taken fully.
Item with weight 20 and profit 100 taken fully.
Item with weight 30 and profit 120 taken partially (Fraction: 0.67).

Maximum Profit: 240.00
```
