import java.util.ArrayList;
import java.util.Collections;

public class solution12910 {

    public int[] solution(int[] arr, int divisor) {
        ArrayList<Integer> temp = new ArrayList<>();

        for (int value : arr) {
            if (value % divisor == 0) {
                temp.add(value);
            }
        }

        if (temp.isEmpty()) {
            temp.add(-1);
        }

        Collections.sort(temp);

        int[] answer = new int[temp.size()];
        for (int i = 0; i < temp.size(); i++) {
            answer[i] = temp.get(i);
        }

        return answer;
    }

}
