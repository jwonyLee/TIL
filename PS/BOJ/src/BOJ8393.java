import java.util.Scanner;

public class BOJ8393 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();

        int sum = 0;
        for (int i=1; i <= n; i++) {
            sum += i;
        }
        System.out.println(sum);
    }
}
