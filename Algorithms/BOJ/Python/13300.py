# https://www.acmicpc.net/problem/13300
# 방 배정
import sys, math

n, k = map(int, sys.stdin.readline().split())
g = [0 for _ in range(7)]
b = [0 for _ in range(7)]
for _ in range(n):
    s, y = map(int, sys.stdin.readline().split())
    if s:
        b[y] += 1
    else:
        g[y] += 1
print(g)
print(b)
gcnt = 0
bcnt = 0
for i in g:
    gcnt += math.ceil(i / k)
for i in b:
    bcnt += math.ceil(i / k)
print(gcnt + bcnt)