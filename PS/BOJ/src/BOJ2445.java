import java.util.Scanner;

public class BOJ2445 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();

        for (int i=0; i < n; i++) {
            for (int j=0; j <= i; j++) {
                System.out.print("*");
            }
            for (int k=0; k < 2; k++) {
                for (int j=0; j < n-i-1; j++) {
                    System.out.print(" ");
                }
            }
            for (int j=0; j <= i; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
        for (int i=0; i < n-1; i++) {
            for (int j=n-i-1; j > 0; j--) {
                System.out.print("*");
            }
            for (int k=0; k < 2; k++) {
                for (int j=0; j <= i; j++) {
                    System.out.print(" ");
                }
            }
            for (int j= n-i-1; j > 0; j--){
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
