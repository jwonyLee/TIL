import java.util.ArrayList;
import java.util.Collections;

class solution42748 {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];

        ArrayList<Integer> temp = new ArrayList<>();

        for (int i = 0; i < commands.length; i++) {
            for (int j = 0; j < commands[i].length; j++) {
                if (j == 0) {
                    for (int k = commands[i][j] -1; k < commands[i][1]; k++) {
                        temp.add(array[k]);
                    }
                    Collections.sort(temp);
                }
            }
            answer[i] = temp.get(commands[i][2] - 1);
            temp.clear();
        }

        return answer;
    }
}