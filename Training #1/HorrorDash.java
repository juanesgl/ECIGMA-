// UVA-11799 - HorrorDash
import java.util.Scanner;

public class HorrorDash {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int numberOfCases = sc.nextInt();

        for (int caseNumber = 1; caseNumber <= numberOfCases; caseNumber++) {
            int numCreatures = sc.nextInt();
            int maxSpeed = -1;

            for (int i = 0; i < numCreatures; i++) {
                int creatureSpeed = sc.nextInt();
                if (creatureSpeed > maxSpeed) {
                    maxSpeed = creatureSpeed;
                }
            }

            System.out.println("Case " + caseNumber + ": " + maxSpeed);
        }

        sc.close();
    }
}
