public class solution12948 {
    public String solution(String phone_number) {
        String [] temp = phone_number.split("");

        for (int i=0; i < temp.length - 4; i++) {
            temp[i] = "*";
        }
        StringBuilder answer = new StringBuilder();
        for (String s : temp) {
            answer.append(s);
        }
        return answer.toString();
    }
}