# https://www.acmicpc.net/problem/11721
# 열 개씩 끊어 출력하기
import sys

word = sys.stdin.readline().strip()

for i in range(0, len(word)):
    print(word[i], end="")
    if (i + 1) % 10 == 0:
        print()
print()