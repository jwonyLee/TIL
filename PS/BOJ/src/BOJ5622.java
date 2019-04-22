import java.util.Scanner;

public class BOJ5622 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String number = in.nextLine().toUpperCase();
        String[][] dialog = {
                {"A", "B", "C"},
                {"D", "E", "F"},
                {"G", "H", "I"},
                {"J", "K", "L"},
                {"M", "N", "O"},
                {"P", "Q", "R", "S"},
                {"T", "U", "V"},
                {"W", "X", "Y", "Z"}
        };
        int result = 0;

        for (int i = 0; i < number.length(); i++) {
            String search = String.valueOf(number.charAt(i));
            int num = 0;
            for (int j = 0; j < dialog.length; j++) {
                for (int k=0; k < dialog[j].length; k++) {
                    if (search.contains(dialog[j][k])) {
                        num += j + 3;
                    }
                }
            }
            result += num;
        }
        System.out.println(result);
    }
}
