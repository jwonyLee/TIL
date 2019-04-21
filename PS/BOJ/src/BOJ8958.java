import java.util.Scanner;

public class BOJ8958 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        in.nextLine();
        for (int i=0; i < n; i++) {
            String result = in.nextLine();
            int[] score = new int[result.length()];
            int cnt = 0;

            for (int j=0; j < result.length(); j++) {
                if (result.charAt(j) == 'O') {
                    cnt++;
                } else {
                    cnt = 0;
                }
                score[j] = cnt;
            }
            int temp = 0;
            for (int j:score) {
                temp += j;
            }
            System.out.println(temp);
        }


    }
}
