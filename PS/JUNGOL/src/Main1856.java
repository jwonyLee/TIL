import java.util.Scanner;

public class Main1856 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(), m = in.nextInt();
        int[][] arr = new int[n][m];
        int k = 1;
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) {
                for (int j = 0; j < m; j++) {
                    arr[i][j] = k++;
                }
            } else {
                for (int j = m - 1; j >= 0; j--) {
                    arr[i][j] = k++;
                }
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j=0; j < m; j++) {
                System.out.print(arr[i][j]+" ");
            }
            System.out.println();
        }
    }
}
