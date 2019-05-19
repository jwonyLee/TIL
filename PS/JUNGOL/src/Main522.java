import java.util.Scanner;

public class Main522 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int a = in.nextInt();
        int b = in.nextInt();

        if (a==b) {
            System.out.println(true);
            System.out.println(false);
        } else {
            System.out.println(false);
            System.out.println(true);
        }
    }
}
