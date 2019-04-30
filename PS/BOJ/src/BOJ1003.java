import java.util.Scanner;

public class BOJ1003 {
    private static int[] f;
    private static int cnt0 = 0;
    private static int cnt1 = 0;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int k = in.nextInt();
        in.nextLine();

        for (int i = 0; i < k; i++) {
            int n = in.nextInt();
            f = new int[n];
            fibonacci(n);
            System.out.println(cnt0 + " " + cnt1);
            cnt0 = 0;
            cnt1 = 0;
        }
    }

    private static int fibonacci(int n) {
        if (n == 0) {
            cnt0++;
            return cnt0;
        } else if (n == 1) {
            cnt1++;
            return cnt1;
        } else {
            if (f[n - 1] == 0) {
                f[n - 1] = fibonacci(n - 2) + fibonacci(n - 1);
                return f[n - 1];
            } else {
                return f[n - 1];
            }
        }
    }
}
