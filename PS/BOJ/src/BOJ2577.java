import java.util.Scanner;

public class BOJ2577 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int a = in.nextInt();
        int b = in.nextInt();
        int c = in.nextInt();
        int result = a * b* c;
        String value = String.valueOf(result);
        int[] cnt = new int[10];

        for (int i=0; i < value.length(); i++) {
            cnt[Integer.parseInt(String.valueOf(value.charAt(i)))]++;
        }

        for (int item : cnt) {
            System.out.println(item);
        }

    }
}
