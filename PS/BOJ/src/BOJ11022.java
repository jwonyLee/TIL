import java.util.Scanner;

public class BOJ11022 {
    public static void main(String[] args) {
        int a, b, T;
        Scanner in = new Scanner(System.in);

        T = in.nextInt();
        for (int i = 0; i < T; i++) {
            a = in.nextInt();
            b = in.nextInt();
            System.out.println("Case #" + (i + 1) + ": " + a + " + " + b + " = " + (a + b));
        }
    }
}
