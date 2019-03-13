import java.util.Scanner;

public class BOJ2440 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();

        for (int i=n; i > 0; i--) {
            for (int j=i; j > 0; j--) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
