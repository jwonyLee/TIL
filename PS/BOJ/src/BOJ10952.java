import java.util.Scanner;

public class BOJ10952 {

    public static void main(String[] args) {
        int a, b;
        Scanner in = new Scanner(System.in);

        while (true) {
            a = in.nextInt();
            b = in.nextInt();
            if (a == 0 && b == 0)
                break;
            System.out.println(a + b);
        }

    }
}
