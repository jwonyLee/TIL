// https://www.acmicpc.net/problem/10951

import java.util.Scanner;

public class BOJ10951 {

    public static void main(String[] args) {
        int a, b;
        Scanner in = new Scanner(System.in);

        while(in.hasNextInt()) {
            a = in.nextInt();
            b = in.nextInt();
            System.out.println(a+b);
        }
    }
}
