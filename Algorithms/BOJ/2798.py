# https://www.acmicpc.net/problem/2798
# 블랙잭
import sys

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
d = []

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            temp = a[i] + a[j] + a[k]
            if temp <= m:
                d.append(temp)

d.sort()
print(d[-1])