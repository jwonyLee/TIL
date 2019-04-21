import java.util.Scanner;

public class BOJ2920 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int[] val = new int[8];
        for (int i = 0; i < val.length; i++) {
            val[i] = in.nextInt();
        }

        int ascending = 1;
        int descending = 8;
        if (val[0] == ascending) {
            for (int value : val) {
                if (ascending == value) {
                    ascending++;
                } else {
                    System.out.println("mixed");
                    break;
                }
            }
        } else if (val[0] == descending) {
            for (int value : val) {
                if (descending == value) {
                    descending--;
                } else {
                    System.out.println("mixed");
                    break;
                }
            }
        } else {
            System.out.println("mixed");
        }

        if (ascending == 9)
            System.out.println("ascending");
        else if (descending == 0)
            System.out.println("descending");
    }
}
