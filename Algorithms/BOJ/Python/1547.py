# https://www.acmicpc.net/problem/1547
# 공
import sys

n = int(sys.stdin.readline())
c = [True, False, False]

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    c[a-1], c[b-1] = c[b-1], c[a-1]

for i in range(len(c)):
    if c[i]:
        print(i+1)