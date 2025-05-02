// UVA-11614 - Etruscan Warriors Never Play Chess

import java.util.Scanner;

public class NeverPlayChess { // Change NeverPlayChess to Main and all the instances that have NeverPlayChess
    public long maxRows(long n) {
        if (n == 0) {
            return 0;
        }

        long low = 1;
        long high = (int) Math.sqrt(2L * n);

        while (low <= high) {

            long mid = (low + high) >> 1;

            long total_warriors = mid * (mid + 1) >> 1;

            if(total_warriors <= n) {
                low = mid + 1;

            } else{
                high = mid - 1;
            }
        }
        return high;
    }

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        int testcases = scanner.nextInt();

        NeverPlayChess solver = new NeverPlayChess();

        while (testcases-- > 0) {

            long warriors = scanner.nextLong();
            System.out.println(solver.maxRows(warriors));
        }
        scanner.close();
    }
}
