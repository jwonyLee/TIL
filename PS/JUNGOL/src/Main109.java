import java.util.Scanner;

public class Main109 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int a = in.nextInt();
        int b = in.nextInt();
        int c = in.nextInt();

        System.out.println(String.format("sum = %d", a+b+c));
        System.out.println(String.format("avg = %d", (a+b+c)/3));
    }
}
