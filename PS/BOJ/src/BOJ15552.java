import java.io.*;

public class BOJ15552 {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));
        String temp = bufferedReader.readLine();
        int T = Integer.parseInt(temp);

        for (int i=0; i < T; i++) {
            temp = bufferedReader.readLine();
            String[] arr = temp.split(" ");
            temp = String.valueOf(Integer.parseInt(arr[0])+Integer.parseInt(arr[1]));
            bufferedWriter.write(temp+"\n");
        }

        bufferedWriter.flush();
    }
}
