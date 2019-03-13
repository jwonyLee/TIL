import java.util.Scanner;

public class BOJ11721 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String text = in.nextLine();
        String[] data = text.split("");
        for (int i=0; i < data.length; i++) {
            System.out.print(data[i]);
            if ((i+1) % 10 == 0)
                System.out.println();
        }
    }
}
