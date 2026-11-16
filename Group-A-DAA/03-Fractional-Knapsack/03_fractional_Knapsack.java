
import java.util.*;

// Class to store details of each item
class Item {

    int weight, profit;  // Item's weight and profit
    double ratio;        // Profit per unit of weight

    // Constructor to initialize item details
    Item(int weight, int profit) {
        this.weight = weight;
        this.profit = profit;

        // Calculate profit/weight ratio
        ratio = (double) profit / weight;
    }
}

public class FractionalKnapsack {

    // Function to solve Fractional Knapsack
    static void knapsack(Item[] items, int capacity) {

        // Sort items by profit/weight ratio in descending order
        Arrays.sort(items,
            (a, b) -> Double.compare(b.ratio, a.ratio));

        double totalProfit = 0;  // Stores maximum profit

        System.out.println("\nSelected Items:");

        // Visit each item after sorting
        for (Item item : items) {

            // Stop if bag is completely full
            if (capacity == 0)
                break;

            // Check if complete item fits in the bag
            if (item.weight <= capacity) {

                // Take the complete item
                capacity -= item.weight;

                // Add complete item's profit
                totalProfit += item.profit;

                // Display selected item details
                System.out.println("Weight: " + item.weight +
                    ", Profit: " + item.profit +
                    ", Fraction: 1.0");
            }

            else {

                // Calculate fraction of item that can be taken
                double fraction =
                    (double) capacity / item.weight;

                // Add fractional profit to total profit
                totalProfit += item.profit * fraction;

                // Display fractional item details
                System.out.println("Weight: " + item.weight +
                    ", Profit: " + item.profit +
                    ", Fraction: " + fraction);

                // Bag is now completely full
                capacity = 0;
            }
        }

        // Display final maximum profit
        System.out.println("\nMaximum Profit = " + totalProfit);
    }

    // Main method: program execution starts here
    public static void main(String[] args) {

        // Scanner to accept user input
        Scanner sc = new Scanner(System.in);

        // Accept number of items
        System.out.print("Enter number of items: ");
        int n = sc.nextInt();

        // Create array to store items
        Item[] items = new Item[n];

        System.out.println("Enter weight and profit of each item:");

        // Accept weight and profit of every item
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

            // Create an Item object and store it in array
            items[i] = new Item(weight, profit);
        }

        // Accept maximum capacity of knapsack
        System.out.print("Enter knapsack capacity: ");
        int capacity = sc.nextInt();

        // Validate capacity
        if (capacity < 0) {
            System.out.println("Invalid capacity!");
        }

        else {
            // Call knapsack function
            knapsack(items, capacity);
        }

        // Close Scanner
        sc.close();
    }
}
/*
Understand the problem
Imagine you have a bag with a maximum capacity of 50 kg.

You have different items, each having:
- Weight
- Profit
Your objective is to select items such that you get maximum profit without exceeding the bag's capacity.

The special feature of Fractional Knapsack is that you can take a fraction of an item.

For example, if an item weighs 30 kg but only 20 kg of space is left, you can take 20/30 of that item.

We calculate:
\[
Ratio = \frac{Profit}{Weight}
\]

Then:
1. Calculate the ratio of every item.
2. Sort items in descending order of ratio.
3. Select the item with the highest ratio.
4. If the complete item fits, take it.
5. Otherwise, take only the fraction that fits.
Remember: We always prioritize maximum profit per unit of weight.

Enter number of items: 3

Enter weight and profit of each item:

Weight of item 1: 10
Profit of item 1: 60

Weight of item 2: 20
Profit of item 2: 100

Weight of item 3: 30
Profit of item 3: 120

Enter knapsack capacity: 50

Selected Items:

Weight: 10, Profit: 60, Fraction: 1.0
Weight: 20, Profit: 100, Fraction: 1.0
Weight: 30, Profit: 120, Fraction: 0.6666666666666666

Maximum Profit = 240.0

*/