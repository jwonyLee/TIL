import java.util.Arrays;
import java.util.Scanner;

public class BOJ1546 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = in.nextInt();
        }

        Arrays.sort(arr);

        float max = arr[arr.length - 1];
        float result = 0;

        for (int value : arr) {
            result += (value / max) * 100;
        }
        System.out.println(result / n);
    }
}
