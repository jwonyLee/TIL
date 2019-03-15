import java.util.Scanner;

public class BOJ2446 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();

        for (int i=0; i < n; i++) {
            for (int j=0; j < i; j++) {
                System.out.print(" ");
            }
            for (int j=0; j < n-i; j++) {
                System.out.print("*");
            }
            for (int j=0; j < n-i-1; j++) {
                System.out.print("*");
            }
            System.out.println();
        }

        for (int i=0; i < n-1; i++) {
            for (int j=n-i-2; j > 0; j--) {
                System.out.print(" ");
            }
            for (int j=0; j <= i+2; j++) {
                System.out.print("*");
            }
            for (int j=0; j < i; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
