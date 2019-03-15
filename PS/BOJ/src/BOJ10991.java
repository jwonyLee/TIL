import java.util.Scanner;

public class BOJ10991 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                System.out.print(" ");
            }
            for (int j = 0; j <= i; j++) {
                System.out.print("*");
                if (j >= 0)
                    System.out.print(" ");
            }
            System.out.println();
        }
    }
}
