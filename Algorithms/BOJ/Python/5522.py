# https://www.acmicpc.net/problem/5522
# 카드 게임
import sys

answer = 0

for _ in range(5):
    answer += int(sys.stdin.readline())
print(answer)