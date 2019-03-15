import java.util.Scanner;

public class BOJ10871 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int x = in.nextInt();
        in.nextLine();
        String s = in.nextLine();
        String[] arr = s.split(" ");

        for (String i:arr) {
            if (Integer.parseInt(i) < x) {
                System.out.print(i+" ");
            }
        }
    }
}
