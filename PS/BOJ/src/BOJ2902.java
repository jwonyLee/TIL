import java.util.Scanner;

public class BOJ2902 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String[] text = in.nextLine().split("-");
        for (String s : text) {
            System.out.print(s.charAt(0));
        }
    }
}
