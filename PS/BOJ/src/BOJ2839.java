import java.util.Scanner;

public class BOJ2839 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int item = in.nextInt();
        int cnt = 0;

        if (item % 5 == 0) {
            System.out.println(item / 5);
        } else {
            cnt = item / 5;
            while (cnt != -1) {
                int temp = item - (cnt * 5);
                if (temp % 3 == 0) {
                    cnt += temp / 3;
                    System.out.println(cnt);
                    break;
                }
                cnt--;
            }
        }

        if (cnt == -1) System.out.println(-1);

    }
}