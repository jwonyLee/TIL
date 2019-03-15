import java.util.Scanner;

public class BOJ10992 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                System.out.print(" ");
            }
            System.out.print("*");
            for (int j = 0; j < i * 2 - 1; j++) {
                if (i!= n-1)
                    System.out.print(" ");
                else
                    System.out.print("*");
            }
            if (i != 0)
                System.out.print("*");
            System.out.println();
        }
    }
}
