import java.util.Scanner;

public class BOJ10818 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int n = in.nextInt();
        int[] data = new int[n];

        for (int i=0; i < data.length; i++) {
            data[i] = in.nextInt();
        }

        int min = data[0];
        int max = data[0];

        for (int i : data) {
            if (min > i)
                min = i;
            if (max < i)
                max = i;
        }

        System.out.println(min+" "+max);
    }
}
