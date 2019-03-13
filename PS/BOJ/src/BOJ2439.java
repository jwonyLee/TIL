import java.util.Scanner;

public class BOJ2439 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();

        for(int i=0; i < n; i++) {
            int t = n - (i+1);
            for (int j=0; j < t; j++) {
                System.out.print(" ");
            }
            for (int j = 1; j <= i+1; j++)
                System.out.print("*");
            System.out.println();
        }
    }
}
