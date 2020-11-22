# https://www.acmicpc.net/problem/11651
# 좌표 정렬하기 2
import sys

n = int(sys.stdin.readline())
a = []

for _ in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))

a.sort(key=lambda x: (x[1], x[0]))
for i in a:
    print(" ".join(map(str, i)))