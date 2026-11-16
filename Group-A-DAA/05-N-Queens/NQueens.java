
import java.util.*;

public class NQueens {

    static int N;
    static int count = 0;

    // Function to print the chessboard
    static void printBoard(int board[][]) {

        count++;

        System.out.println("\nSolution " + count + ":");

        for (int i = 0; i < N; i++) {

            for (int j = 0; j < N; j++) {

                System.out.print(board[i][j] + " ");
            }

            System.out.println();
        }
    }

    // Function to check whether queen can be placed safely
    static boolean isSafe(int board[][], int row, int col) {

        // CHECK 1: Check left side of current row
        for (int j = 0; j < col; j++) {

            if (board[row][j] == 1)
                return false;
        }

        // CHECK 2: Check upper-left diagonal
        for (int i = row, j = col;
             i >= 0 && j >= 0;
             i--, j--) {

            if (board[i][j] == 1)
                return false;
        }

        // CHECK 3: Check lower-left diagonal
        for (int i = row, j = col;
             i < N && j >= 0;
             i++, j--) {

            if (board[i][j] == 1)
                return false;
        }

        return true;
    }

    // Function to solve N-Queens using Backtracking
    static void solveNQueens(int board[][], int col) {

        // BASE CONDITION: All queens are placed
        if (col >= N) {

            printBoard(board);
            return;
        }

        // Try placing queen in every row
        for (int i = 0; i < N; i++) {

            // Check whether current position is safe
            if (isSafe(board, i, col)) {

                // Place queen
                board[i][col] = 1;

                // Recursively solve next column
                solveNQueens(board, col + 1);

                // BACKTRACKING: Remove queen
                board[i][col] = 0;
            }
        }
    }

    // Main method
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // Accept number of queens
        System.out.print("Enter value of N: ");
        N = sc.nextInt();

        // Validate N
        if (N < 1) {

            System.out.println("Invalid value of N!");

            sc.close();
            return;
        }

        // Create N x N chessboard
        int board[][] = new int[N][N];

        // Start solving from first column
        solveNQueens(board, 0);

        // Display total number of solutions
        if (count == 0) {

            System.out.println("\nSolution does not exist!");

        } else {

            System.out.println("\nTotal Solutions: " + count);
        }

        sc.close();
    }
}
