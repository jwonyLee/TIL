# https://www.acmicpc.net/problem/9095
# 1, 2, 3 더하기
import sys 

d = [0 for _ in range(12)]
d[0] = 1
d[1] = 1

for i in range(2, 12):
    d[i] = d[i-1] + d[i-2] + d[i-3]

n = int(sys.stdin.readline())

for _ in range(n):
    x = int(sys.stdin.readline())
    print(d[x])