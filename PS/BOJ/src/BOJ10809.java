import java.util.Scanner;

public class BOJ10809 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String text = in.nextLine().toLowerCase();
        int[] index = new int[26];

        for (int i=0; i < index.length; i++) {
            index[i] = -1;
        }
        for (int i=0; i < text.length(); i++) {
            int temp = (int) text.charAt(i);
            temp -= 97;
            if (index[temp] == -1) {
                index[temp] = i;
            }
        }

        for (int i:index) {
            System.out.print(i+" ");
        }
    }
}
