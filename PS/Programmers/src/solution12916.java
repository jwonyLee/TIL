public class solution12916 {
    boolean solution(String s) {
        boolean answer = true;

        String test = s.toUpperCase();

        int cntP = 0;
        int cntY = 0;

        for (int i=0; i < test.length(); i++) {
            if (test.charAt(i) == 'P') cntP++;
            if (test.charAt(i) == 'Y') cntY++;
        }

        if (cntP != cntY) answer = false;

        return answer;
    }
}