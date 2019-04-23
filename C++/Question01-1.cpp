#include <iostream>

int main(void) {
    int arr[5];
    int result = 0;

    for (int i=0; i < sizeof(arr) / sizeof(arr[0]); i++) {
        std::cout << i+1 << "번째 정수 입력: ";
        std::cin >> arr[i];
        result += arr[i];
    }

    std::cout << "합계: " << result;
}