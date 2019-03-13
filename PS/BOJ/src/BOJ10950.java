// https://www.acmicpc.net/problem/10950
import java.util.Scanner;

public class BOJ10950 {
    public static void main(String[] args) {
        int a, b, T;
        Scanner in = new Scanner(System.in);

        // Test Case 개수 입력
        T = in.nextInt();

        for (int i=0; i < T; i++) {
            a = in.nextInt();
            b = in.nextInt();
            System.out.println(a+b);
        }
    }
}
