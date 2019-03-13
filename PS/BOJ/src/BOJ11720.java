import java.util.Scanner;

public class BOJ11720 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        // 숫자의 개수
        int T = in.nextInt();
        in.nextLine(); // nextInt() 뒤에 nextLine() 사용 시 씹히는 걸 방지(버퍼 제거)
        String text = in.nextLine();
        String[] data = text.split("");
        int sum = 0;
        for (int i=0; i < T; i++) {
            sum += Integer.parseInt(data[i]);
        }
        System.out.println(sum);
    }
}
