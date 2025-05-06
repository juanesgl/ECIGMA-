// UVA 11507 - Bender B. Rodríguez Problem
import java.util.Scanner;

public class benderBRodriguez {
    private static String rotate(String current, String bend) {
        switch (current) {
            case "+x":
                return bend;
            case "-x":
                return bend.equals("+y") ? "-y" : bend.equals("-y") ? "+y" : bend.equals("+z") ? "-z" : "+z";
            case "+y":
                return bend.equals("+y") ? "-x" : bend.equals("-y") ? "+x" : "+y";
            case "-y":
                return bend.equals("+y") ? "+x" : bend.equals("-y") ? "-x" : "-y";
            case "+z":
                return bend.equals("+z") ? "-x" : bend.equals("-z") ? "+x" : "+z";
            case "-z":
                return bend.equals("+z") ? "+x" : bend.equals("-z") ? "-x" : "-z";
            default:
                return current;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int L = sc.nextInt();

        while (L != 0) {
            String direction = "+x";

            for (int i = 0; i < L - 1; i++) {
                String bend = sc.next();
                if (!bend.equals("No")) {
                    direction = rotate(direction, bend);
                }
            }

            System.out.println(direction);
            L = sc.nextInt();
        }

        sc.close();
    }
}
