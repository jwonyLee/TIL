import java.util.Scanner;

public class BOJ2675 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        in.nextLine();

        for (int i = 0; i < n; i++) {
            String text = in.nextLine();
            int repeat = Integer.parseInt(String.valueOf(text.charAt(0)));
            for (int j=2; j < text.length(); j++) {
                for (int k=0; k < repeat; k++) {
                    System.out.print(text.charAt(j));
                }
            }
            System.out.println();
        }
    }
}
