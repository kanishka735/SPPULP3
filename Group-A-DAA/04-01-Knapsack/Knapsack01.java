
import java.util.*;

public class Knapsack01 {

    /*
     PROBLEM STATEMENT:
     Implement 0/1 Knapsack using Dynamic Programming.
     Select items to maximize profit without exceeding
     the given knapsack capacity.

     THEORY:
     In 0/1 Knapsack, each item can either be selected
     completely (1) or rejected (0).
     Dynamic Programming stores subproblem results
     in a 2D table to avoid repeated calculations.

     ALGORITHM:
     1. Accept number of items, weights and profits.
     2. Accept knapsack capacity.
     3. Create a 2D DP table.
     4. Initialize first row and column with zero.
     5. Check whether the current item fits.
     6. Calculate profit by including or excluding it.
     7. Store maximum profit in the DP table.
     8. Trace the table backwards to find selected items.
     9. Display maximum profit.

     SAMPLE INPUT:
     Number of items: 3
     Weights: 10 20 30
     Profits: 60 100 120
     Capacity: 50

     EXPECTED OUTPUT:
     Selected Items: 3 and 2
     Maximum Profit = 220

     UBUNTU COMMANDS:
     javac Knapsack01.java
     java Knapsack01

     TIME COMPLEXITY: O(n * W)
     SPACE COMPLEXITY: O(n * W)
    */

    // Function to solve Knapsack using Dynamic Programming
    static int knapsack(int W, int wt[], int val[], int n) {

        // Create DP table for items and capacities
        int dp[][] = new int[n + 1][W + 1];

        // Fill DP table using nested loops
        for (int i = 0; i <= n; i++) {

            for (int w = 0; w <= W; w++) {

                // Base condition: no items or zero capacity
                if (i == 0 || w == 0) {
                    dp[i][w] = 0;
                }

                // Check whether current item fits
                else if (wt[i - 1] <= w) {

                    // Include or exclude current item
                    dp[i][w] = Math.max(

                        // Include item and add remaining capacity profit
                        val[i - 1] +
                        dp[i - 1][w - wt[i - 1]],

                        // Exclude current item
                        dp[i - 1][w]
                    );
                }

                else {

                    // Item does not fit, so exclude it
                    dp[i][w] = dp[i - 1][w];
                }
            }
        }

        // Display selected items by tracing DP table backwards
        System.out.println("\nSelected Items:");

        int w = W;

        // Start from last item and move backwards
        for (int i = n; i > 0 && w > 0; i--) {

            // If values differ, current item was selected
            if (dp[i][w] != dp[i - 1][w]) {

                System.out.println("Item " + i +
                    " - Weight: " + wt[i - 1] +
                    ", Profit: " + val[i - 1]);

                // Reduce remaining capacity
                w = w - wt[i - 1];
            }
        }

        // Return maximum profit
        return dp[n][W];
    }

    // Main method: execution starts here
    public static void main(String[] args) {

        // Scanner to accept user input
        Scanner sc = new Scanner(System.in);

        // Accept number of items
        System.out.print("Enter number of items: ");
        int n = sc.nextInt();

        // Validate number of items
        if (n <= 0) {
            System.out.println("Invalid number of items!");
            sc.close();
            return;
        }

        // Arrays to store weights and profits
        int wt[] = new int[n];
        int val[] = new int[n];

        // Accept weight and profit of every item
        System.out.println("Enter weight and profit of each item:");

        for (int i = 0; i < n; i++) {

            System.out.print("Weight of item " + (i + 1) + ": ");
            wt[i] = sc.nextInt();

            System.out.print("Profit of item " + (i + 1) + ": ");
            val[i] = sc.nextInt();

            // Validate item details
            if (wt[i] <= 0 || val[i] < 0) {
                System.out.println("Invalid input!");
                sc.close();
                return;
            }
        }

        // Accept maximum knapsack capacity
        System.out.print("Enter knapsack capacity: ");
        int W = sc.nextInt();

        // Validate capacity
        if (W < 0) {
            System.out.println("Invalid capacity!");
        }

        else {

            // Call Dynamic Programming function
            int maxProfit = knapsack(W, wt, val, n);

            // Display maximum profit
            System.out.println("\nMaximum Profit = " + maxProfit);
        }

        // Close Scanner
        sc.close();
    }
}
