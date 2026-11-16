
import java.util.Scanner;

public class Main {

    // Non-Recursive (Iterative) Fibonacci
    static long[] fibonacciIterative(int n) {

        long[] result = new long[n];

        long a = 0, b = 1, c;

        for (int i = 0; i < n; i++) {
            result[i] = a;

            c = a + b;
            a = b;
            b = c;
        }

        return result;
    }

    // Recursive Fibonacci
    static long fibonacciRecursive(int n) {

        if (n == 0)
            return 0;

        if (n == 1)
            return 1;

        return fibonacciRecursive(n - 1)
             + fibonacciRecursive(n - 2);
    }

    // Generate Recursive Fibonacci Series
    static long[] fibonacciRecursiveSeries(int n) {

        long[] result = new long[n];

        for (int i = 0; i < n; i++) {
            result[i] = fibonacciRecursive(i);
        }

        return result;
    }

    // Display Series
    static void display(long[] result) {

        System.out.println("Fibonacci Series:");

        for (long num : result) {
            System.out.print(num + " ");
        }

        System.out.println();
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int choice, n;

        do {
            System.out.println("\n===== FIBONACCI MENU =====");
            System.out.println("1. Non-Recursive Fibonacci");
            System.out.println("2. Recursive Fibonacci");
            System.out.println("3. Exit");

            System.out.print("Enter your choice: ");
            choice = sc.nextInt();

            switch (choice) {

                case 1:
                    System.out.print("Enter number of terms (0-93): ");
                    n = sc.nextInt();

                    if (n < 0 || n > 93) {
                        System.out.println("Enter a number between 0 and 93.");
                        break;
                    }

                    long start1 = System.nanoTime();

                    long[] iterative = fibonacciIterative(n);

                    long end1 = System.nanoTime();

                    display(iterative);

                    long time1 = end1 - start1;

                    System.out.printf("Execution Time: %.6f ms%n",
                            time1 / 1000000.0);

                    System.out.println("Time Complexity: O(n)");
                    System.out.println("Auxiliary Space Complexity: O(1)");
                    break;

                case 2:
                    System.out.print("Enter number of terms (0-93): ");
                    n = sc.nextInt();

                    if (n < 0 || n > 93) {
                        System.out.println("Enter a number between 0 and 93.");
                        break;
                    }

                    long start2 = System.nanoTime();

                    long[] recursive = fibonacciRecursiveSeries(n);

                    long end2 = System.nanoTime();

                    display(recursive);

                    long time2 = end2 - start2;

                    System.out.printf("Execution Time: %.6f ms%n",
                            time2 / 1000000.0);

                    System.out.println("Time Complexity: O(2^n)");
                    System.out.println("Auxiliary Space Complexity: O(n)");
                    break;

                case 3:
                    System.out.println("Program Exited.");
                    break;

                default:
                    System.out.println("Invalid choice! Try again.");
            }

        } while (choice != 3);

        sc.close();
    }
}
