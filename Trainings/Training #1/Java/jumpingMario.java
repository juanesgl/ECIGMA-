// UVA 117564 - Jumping Mario
import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;
public class jumpingMario {


    public static int[] calc(List<Integer> arr){

        int h = arr.get(0);
        int high = 0;
        int low = 0;

        for (int i = 0; i < arr.size(); i++) {

            int height = arr.get(i);
            if (height > h) {
                high++;
            }else if (height < h){
                low++;
            }
        }
        return new int[]{high,low};
    }

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        int t = scanner.nextInt();

        for (int i = 0; i < t; i++) {
            int n = scanner.nextInt();
            List<Integer> nums = new ArrayList<>();

            for (int j = 0; j < n; j++) {
                nums.add(scanner.nextInt());
            }
            int[] result = calc(nums);
            System.out.printf("Case %d: %d %d%n", i + 1, result[0], result[1]);
        }
        scanner.close();
    }

}
