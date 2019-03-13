import java.util.Scanner;

public class BOJ10953 {
    public static void main(String[] args) {
        int T;
        String text;
        Scanner in = new Scanner(System.in);

        T = in.nextInt();

        for (int i=0; i < T; i++) {
            text = in.next();
            String data[] = text.split(",");
            System.out.println(Integer.parseInt(data[0])+Integer.parseInt(data[1]));
        }
    }
}
