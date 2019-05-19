import java.util.Scanner;

public class Main1291 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int s = in.nextInt();
        int e = in.nextInt();

        while (s < 2 || s > 9 || e < 2 || e > 9) {
            System.out.println("INPUT ERROR!");
            s = in.nextInt();
            e = in.nextInt();
        }
        if (s >= e) {
            for (int i = 1; i < 10; i++) {
                for (int j = s; j >= e; j--) {
                    System.out.print(String.format("%d * %d = %2d   ", j, i, j * i));
                }
                System.out.println();
            }
        } else {
            for (int i = 1; i < 10; i++) {
                for (int j = s; j <= e; j++) {
                    System.out.print(String.format("%d * %d = %2d   ", j, i, j * i));
                }
                System.out.println();
            }
        }

    }
}
