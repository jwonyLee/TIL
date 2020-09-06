# https://www.acmicpc.net/problem/13410
# 거꾸로 구구단
import sys

n, k = map(int, sys.stdin.readline().split())

m = []

for i in range(1, k+1):
    m.append(int(str(i * n)[::-1]))

print(max(m))