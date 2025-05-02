// UVA-10071 - Back to High School Physics
import java.util.Scanner;

public class backtohsphysics { //Change backtohsphysics to Main when running in VJudge

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        while(scanner.hasNextInt()){
            int v = scanner.nextInt();
            int t = scanner.nextInt();
            System.out.println(2 * v * t);
        }
        scanner.close();
    }
}