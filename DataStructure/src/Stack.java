public class Stack {
    private static int top = -1;
    private static final int STACK_SIZE = 100;

    private static int stack[] = new int[STACK_SIZE];

    public static void main(String[] args) {
        System.out.println("**순차 스택 연산**");
        printStack();
        push(1); printStack();
        push(2); printStack();
        push(3); printStack();

        System.out.print("peek => " + peek()); // 현재 top의 원소 출력
        printStack();
        System.out.print("pop => " + pop()); // 삭제
        printStack();
        System.out.print("pop => " + pop()); // 삭제
        printStack();
        System.out.print("pop => " + pop()); // 삭제

    }

    // Stack 공백 상태 확인
    private static boolean isEmpty() {
        if (top == -1) return true;
        else return false;
    }

    // Stack 포화 상태 확인
    private static boolean isFull() {
        if (top == STACK_SIZE - 1) return true;
        else return false;
    }

    // Stack의 top에 원소를 삽입하는 연산
    private static void push(int item) {
        if (isFull()) {
            System.out.println("Stack is Full!");
        } else {
            stack[++top] = item;
        }
    }

    // Stack의 top에서 원소를 삭제하는 연산
    private static int pop() {
        if (isEmpty()) {
            System.out.println("Stack is Empty!");
            return 0;
        } else {
            return stack[top--];
        }
    }

    // Stack의 top 원소를 검색하는 연산
    private static int peek() {
        if (isEmpty()) {
            System.out.println("Stack is Empty!");
            return 0;
        } else {
            return stack[top];
        }
    }

    // Stack의 원소를 출력하는 연산
    private static void printStack() {
        System.out.print("\nstack = [ ");
        for (int i=0; i <= top; i++) {
            System.out.print(stack[i] + " ");
        }
        System.out.print("]  ");
    }

}