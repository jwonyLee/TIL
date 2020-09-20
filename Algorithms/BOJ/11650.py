# https://www.acmicpc.net/problem/11650
# 좌표 정렬하기
import sys

n = int(sys.stdin.readline())
a = []

for _ in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))

a.sort()
for i in a:
    print(" ".join(map(str, i)))