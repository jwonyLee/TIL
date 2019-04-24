import java.util.Scanner;

public class BOJ2475 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String[] number = in.nextLine().split(" ");
        int result = 0;
        for (String s:number) {
            result += Integer.parseInt(s) * Integer.parseInt(s);
        }
        System.out.println(result % 10);
    }
}
