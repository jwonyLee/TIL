import java.util.Scanner;

public class BOJ4344 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int C = in.nextInt();
        in.nextLine();

        for (int i = 0; i < C; i++) {
            String temp = in.nextLine();
            String[] tempArr = temp.split(" ");
            float result = 0;
            for (int j = 1; j < tempArr.length; j++) {
                result += Float.parseFloat(tempArr[j]);
            }
            result = result / Float.parseFloat(tempArr[0]);
            int cnt = 0;
            for (int j = 1; j < tempArr.length; j++) {
                if (Float.parseFloat(tempArr[j]) > result)
                    cnt++;
            }
            result = (float) (cnt / Float.parseFloat(tempArr[0]) * 100.0);
            System.out.println(String.format("%.3f",result)+"%");
//             System.out.println(result/Float.parseFloat(tempArr[0])+"%");
        }
    }
}
