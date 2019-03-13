import java.util.Scanner;

public class BOJ2438 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();

        for(int i=0; i < n; i++) {
            for (int j = 1; j <= i+1; j++)
                System.out.print("*");
            System.out.println();
        }
    }
}
