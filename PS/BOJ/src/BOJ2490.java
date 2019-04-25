import java.util.Scanner;

public class BOJ2490 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int[] arr = new int[4];
        int cnt = 0;

        for (int i=0; i < 3; i++) {
            for (int j=0; j < arr.length; j++) {
                arr[j] = in.nextInt();
            }
            for (int value : arr) {
                if (value == 0) cnt++;
            }

            switch(cnt) {
                case 1:
                    System.out.println("A");
                    break;
                case 2:
                    System.out.println("B");
                    break;
                case 3:
                    System.out.println("C");
                    break;
                case 4:
                    System.out.println("D");
                    break;
                case 0:
                    System.out.println("E");
                    break;
            }
            cnt = 0;
        }
    }
}
