import java.util.Scanner;

public class BOJ2442 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();

        for (int i=1; i <= n; i++) {
            for (int j=n-1; j >= i; j--) {
                System.out.print(" ");
            }
           for (int j=0; j <= 2*(i-1); j++) {
               System.out.print("*");
           }
            System.out.println();
        }
    }
}
