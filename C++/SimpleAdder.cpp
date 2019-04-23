#include <iostream>

int main(void) {
    int val1;
    std::cout << "첫 번째 숫자입력: ";
    std::cin >> val1;

    int val2;
    std::cout << "두 번째 숫자입력: ";
    std::cin >> val2;

    int result = val1 + val2;
    std::cout << "덧셈결과: " << result << std::endl;
    return 0;
}