# https://www.acmicpc.net/problem/4641
# Doubles
import sys

while True:
    n = list(map(int, sys.stdin.readline().split()))

    if n[0] == -1:
        break

    n.sort()

    answer = 0

    for i in range(1, len(n)):
        if n[i] * 2 in n:
            answer += 1

    print(answer)