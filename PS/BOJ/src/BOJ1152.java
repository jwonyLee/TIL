import java.util.Scanner;

public class BOJ1152 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String text = in.nextLine().trim();

        if (text.isEmpty())
            System.out.println(0);
        else {
            String[] word = text.split(" ");
            System.out.println(word.length);
        }
    }
}
