import java.util.Scanner;

public class Main516 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        double a = in.nextDouble();
        double b = in.nextDouble();
        char c = in.next().charAt(0);

        System.out.println(String.format("%.2f", a));
        System.out.println(String.format("%.2f", b));
        System.out.println(c);
    }
}
