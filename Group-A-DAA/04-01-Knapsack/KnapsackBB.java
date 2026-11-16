
import java.util.*;

public class KnapsackBB {

    /*
     PROBLEM STATEMENT:
     Implement 0/1 Knapsack using Branch and Bound.
     Maximize profit without exceeding knapsack capacity.

     THEORY:
     Branch and Bound is an optimization technique
     that explores possible solutions using a State
     Space Tree.

     BRANCHING:
     1. Include current item.
     2. Exclude current item.

     BOUNDING:
     Calculate an upper bound to estimate the maximum
     possible profit of a branch.

     PRUNING:
     Discard branches whose upper bound cannot improve
     the current maximum profit.

     ALGORITHM:
     1. Accept item details and capacity.
     2. Sort items by profit/weight ratio.
     3. Create a root node.
     4. Calculate its upper bound.
     5. Insert root into PriorityQueue.
     6. Select the node having highest bound.
     7. Create include and exclude child nodes.
     8. Calculate upper bound for each child.
     9. Prune unpromising branches.
     10. Display selected items and maximum profit.

     SAMPLE INPUT:
     Number of items: 3
     Weights: 10 20 30
     Profits: 60 100 120
     Capacity: 50

     EXPECTED OUTPUT:
     Maximum Profit = 220

     UBUNTU COMMANDS:
     javac KnapsackBB.java
     java KnapsackBB

     TIME COMPLEXITY: O(2^n) worst case
     SPACE COMPLEXITY: O(2^n) worst case
    */

    // Class to store item details
    static class Item {

        int weight, profit;
        double ratio;

        // Constructor to initialize item
        Item(int weight, int profit) {

            this.weight = weight;
            this.profit = profit;

            // Calculate profit/weight ratio
            this.ratio = (double) profit / weight;
        }
    }

    // Class representing a node in the State Space Tree
    static class Node {

        int level;                 // Current item index
        int profit;                // Total profit
        int weight;                // Total weight
        double bound;              // Upper bound
        ArrayList<Integer> selected; // Selected item indexes
    }

    // Store maximum profit
    static int maxProfit = 0;

    // Store indexes of selected items
    static ArrayList<Integer> bestItems = new ArrayList<>();

    // Function to calculate upper bound
    static double bound(Node node, Item[] items, int W, int n) {

        // Return zero if weight exceeds capacity
        if (node.weight > W)
            return 0;

        // Initialize upper bound with current profit
        double profitBound = node.profit;

        // Initialize current weight
        int totalWeight = node.weight;

        // Start checking next item
        int j = node.level + 1;

        // Add complete items while capacity permits
        while (j < n &&
               totalWeight + items[j].weight <= W) {

            totalWeight += items[j].weight;
            profitBound += items[j].profit;

            j++;
        }

        // Add fraction of next item for upper bound only
        if (j < n) {

            profitBound +=
                (W - totalWeight) * items[j].ratio;
        }

        // Return calculated upper bound
        return profitBound;
    }

    // Function to solve Knapsack using Branch and Bound
    static void knapsack(Item[] items, int W, int n) {

        // Sort items in descending order of profit/weight ratio
        Arrays.sort(items,
            (a, b) -> Double.compare(b.ratio, a.ratio));

        // Create PriorityQueue with highest bound first
        PriorityQueue<Node> pq =
            new PriorityQueue<>(
                (a, b) -> Double.compare(b.bound, a.bound)
            );

        // Create root node
        Node root = new Node();

        root.level = -1;
        root.profit = 0;
        root.weight = 0;

        // Initially no items are selected
        root.selected = new ArrayList<>();

        // Calculate root upper bound
        root.bound = bound(root, items, W, n);

        // Insert root into PriorityQueue
        pq.add(root);

        // Initialize maximum profit and selected items
        maxProfit = 0;
        bestItems = new ArrayList<>();

        // Explore promising nodes
        while (!pq.isEmpty()) {

            // Remove node having highest upper bound
            Node u = pq.poll();

            // Prune node if it cannot improve current profit
            if (u.bound <= maxProfit)
                continue;

            // Find next item to consider
            int next = u.level + 1;

            // Stop if all items are processed
            if (next >= n)
                continue;

            // ---------------------------------
            // BRANCH 1: INCLUDE CURRENT ITEM
            // ---------------------------------

            // Create include node
            Node include = new Node();

            include.level = next;

            // Add current item weight
            include.weight =
                u.weight + items[next].weight;

            // Add current item profit
            include.profit =
                u.profit + items[next].profit;

            // Copy previously selected items
            include.selected =
                new ArrayList<>(u.selected);

            // Add current item index
            include.selected.add(next);

            // Update maximum profit if capacity is valid
            if (include.weight <= W &&
                include.profit > maxProfit) {

                maxProfit = include.profit;

                // Store best selected items
                bestItems =
                    new ArrayList<>(include.selected);
            }

            // Calculate upper bound of include node
            include.bound =
                bound(include, items, W, n);

            // Insert promising include node
            if (include.weight <= W &&
                include.bound > maxProfit) {

                pq.add(include);
            }

            // ---------------------------------
            // BRANCH 2: EXCLUDE CURRENT ITEM
            // ---------------------------------

            // Create exclude node
            Node exclude = new Node();

            exclude.level = next;

            // Weight remains unchanged
            exclude.weight = u.weight;

            // Profit remains unchanged
            exclude.profit = u.profit;

            // Copy previously selected items
            exclude.selected =
                new ArrayList<>(u.selected);

            // Calculate upper bound
            exclude.bound =
                bound(exclude, items, W, n);

            // Insert only promising exclude node
            if (exclude.bound > maxProfit) {

                pq.add(exclude);
            }
        }

        // Display selected items
        System.out.println("\nSelected Items:");

        for (int index : bestItems) {

            System.out.println(
                "Weight: " + items[index].weight +
                ", Profit: " + items[index].profit
            );
        }

        // Display maximum profit
        System.out.println("\nMaximum Profit = " + maxProfit);
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

        // Create array of Item objects
        Item[] items = new Item[n];

        // Accept item details
        System.out.println("Enter weight and profit of each item:");

        for (int i = 0; i < n; i++) {

            System.out.print("Weight of item " + (i + 1) + ": ");
            int weight = sc.nextInt();

            System.out.print("Profit of item " + (i + 1) + ": ");
            int profit = sc.nextInt();

            // Validate weight and profit
            if (weight <= 0 || profit < 0) {

                System.out.println("Invalid input!");

                sc.close();
                return;
            }

            // Create and store Item object
            items[i] = new Item(weight, profit);
        }

        // Accept knapsack capacity
        System.out.print("Enter knapsack capacity: ");
        int W = sc.nextInt();

        // Validate capacity
        if (W < 0) {

            System.out.println("Invalid capacity!");

        } else {

            // Call Branch and Bound function
            knapsack(items, W, n);
        }

        // Close Scanner
        sc.close();
    }
}
