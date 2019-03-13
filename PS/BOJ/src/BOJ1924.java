// https://blockdmask.tistory.com/247 블로그 문제 풀이 참고하였음

import java.util.Scanner;

public class BOJ1924 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        String[] days = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
        int[] date = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

        int month = in.nextInt();
        int day = in.nextInt();
        int dday = 0;

        for (int i = 0; i <= month - 1; i++) {
            dday += date[i];
        }
        dday -= date[month - 1] - day;
        System.out.println(days[dday % 7]);
    }
}
