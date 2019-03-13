// https://www.acmicpc.net/problem/10951
// 문제 후기 https://j-archives.tistory.com/28

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
