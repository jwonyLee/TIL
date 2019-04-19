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
}
