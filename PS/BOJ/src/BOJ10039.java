import java.util.Scanner;

public class BOJ10039 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int[] score = new int[5];
        int result = 0;

        for (int i=0; i < score.length; i++) {
            score[i] = in.nextInt();
        }

        for (int val : score) {
            if (val < 40) {
                result += 40;
            } else {
                result += val;
            }
        }

        System.out.println(result/5);
    }
}
