import java.util.Scanner;

public class BOJ2908 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String[] data = in.nextLine().split(" ");
        String[] result = new String[data.length];

        for (int i=0; i < result.length; i++) {
            result[i] = "";
        }

        for (int i=0; i < data.length; i++) {
            for (int j=data[i].length()-1; j >= 0; j--) {
                result[i] += data[i].charAt(j);
            }
        }

        if (Integer.parseInt(result[0]) > Integer.parseInt(result[1])) System.out.println(result[0]);
        else System.out.println(result[1]);
    }
}
