import java.util.ArrayList;
import java.util.Scanner;

public class BOJ2501 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int k = in.nextInt();
        ArrayList<Integer> prime = new ArrayList<>();

        for (int i = 1; i <= n; i++) {
            if (n % i == 0) {
                prime.add(i);
            }
        }

        if (k > prime.size()) System.out.println(0);
        else System.out.println(prime.get(k - 1));
    }
}
