import java.util.Scanner;

public class BOJ2750 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] arr = new int[n];

        for (int i=0; i < n; i++) {
            arr[i] = in.nextInt();
        }

        for (int i=0; i < arr.length; i++) {
            for (int j=0; j < arr.length-i - 1; j++) {
                if (arr[j] > arr[j+1]) {
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
        }
        for (int value : arr) {
            System.out.println(value);
        }
    }
}