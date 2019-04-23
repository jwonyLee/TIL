import java.util.Scanner;

public class BOJ2609 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int a = in.nextInt();
        int b = in.nextInt();

        System.out.println(gcd(a, b));
        System.out.println(lcm(a, b));
    }

    private static int gcd(int a, int b) {
        if (a < b) {
            int temp = a;
            a = b;
            b = temp;
        }

        while (b != 0) {
            int n = a % b;
            a = b;
            b = n;
        }

        return a;
    }

    private static int lcm(int a, int b) {
        return a * b / gcd(a, b);
    }
}
