import java.util.ArrayList;
import java.util.Scanner;

public class BOJ10828 {
    private static ArrayList<Integer> stack = new ArrayList<>();
    private static int index = -1;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        in.nextLine();

        for (int i=0; i < n; i++) {
            String[] menu = in.nextLine().split(" ");
            switch (menu[0]) {
                case "push":
                    push(Integer.parseInt(menu[1]));
                    break;
                case "pop":
                    System.out.println(pop());
                    break;
                case "size":
                    System.out.println(size());
                    break;
                case "empty":
                    System.out.println(empty());
                    break;
                case "top":
                    System.out.println(top());
                    break;
            }
        }
    }
    private static void push(int x) {
        stack.add(x);
        index++;
    }
    private static int pop() {
        if (!stack.isEmpty()) {
            int pop = stack.get(index);
            stack.remove(index);
            index--;
            return pop;
        } else {
            return -1;
        }
    }
    private static int size() {
        return stack.size();
    }
    private static int empty() {
        if (stack.isEmpty()) return 1;
        else return 0;
    }
    private static int top() {
        if (stack.isEmpty()) return -1;
        else return stack.get(index);
    }
}
