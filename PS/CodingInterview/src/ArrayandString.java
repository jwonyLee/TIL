/* 배열과 문자열 해법 */

public class ArrayandString {
    /* 1.1 중복이 없는가
     * - ASCII 문자열이라고 가정
     */
    boolean isUniqueChars(String str) {
        if (str.length() > 128) return false;
        boolean[] char_set = new boolean[128]; // boolean 배열의 경우 생성 시 false로 초기화
        for (int i = 0; i < str.length(); i++) {
            int val = str.charAt(i);
            if (char_set[val]) { // 이 문자는 이미 문자열 내에 있음
                return false;
            }
            char_set[val] = true;
        }
        return true;
    }

    /* 1.1 중복이 없는가
     * - 소문자 a부터 z까지 구성된다고 가정
     * - 비트 벡터 사용
     */
    boolean isUniqueChars2(String str) {
        int checker = 0;
        for (int i = 0; i < str.length(); i++) {
            int val = str.charAt(i) - 'a';
            if ((checker & (1 << val)) > 0) {
                return false;
            }
            checker |= (1 << val);
        }
        return true;
    }

    /* 1.2 순열 확인 */
    /* 두 문자열이 서로 순열 관계라면 -> 같은 문자로 구성 & 순서만 다름 */
    private String sort(String s) {
        char[] content = s.toCharArray();
        java.util.Arrays.sort(content);
        return new String(content);
    }

    public boolean permutation(String s, String t) {
        if (s.length() != t.length()) return false; // 두 문자열이 순열이라면 문자열의 길이가 같아야 함.
        return sort(s).equals(sort(t));
    }

    /* 1.2 순열 확인
    - 문자열에 포함된 문자의 출현 횟수가 같은지 검사
     */

    boolean permutation2(String s, String t) {
        if (s.length() != t.length()) return false;

        int[] letters = new int[128]; // 가정

        char[] s_array = s.toCharArray();
        for (char c : s_array) { // s 내에서 각 문자의 출현 횟수를 센다.
            letters[c]++;
        }

        for (int i = 0; i < t.length(); i++) {
            int c = (int) t.charAt(i);
            letters[c]--;
            if (letters[c] < 0) {
                return false;
            }
        }
        return true;
    }

    /* 1.6 문자열 압축 */
    String compressBad(String str) {
        String compressedString = "";
        int countConsecutive = 0;
        for (int i = 0; i < str.length(); i++) {
            countConsecutive++;

            /* 다음 문자와 현재 문자가 같지 않다면 현재 문자를 결과 문자열에 추가한다. */
            if (i + 1 >= str.length() || str.charAt(i) != str.charAt(i + 1)) {
                compressedString += "" + str.charAt(i) + countConsecutive;
                countConsecutive = 0;
            }
        }
        return compressedString.length() < str.length() ? compressedString : str;
    }

    String compress(String str) {
        StringBuilder compressed = new StringBuilder();
        int countConsecutive = 0;
        for (int i = 0; i < str.length(); i++) {
            countConsecutive++;

            /* 다음 문자와 현재 문자가 같지 않다면 현재 문자를 결과 문자열에 추가한다. */
            if (i + 1 >= str.length() || str.charAt(i) != str.charAt(i + 1)) {
                compressed.append(str.charAt(i));
                compressed.append(countConsecutive);
                countConsecutive = 0;
            }
        }
        return compressed.length() < str.length() ? compressed.toString() : str;
    }
}
