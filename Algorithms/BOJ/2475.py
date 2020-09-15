# https://www.acmicpc.net/problem/2475
# 검증수
import sys

n = list(map(int, sys.stdin.readline().split()))

for i in range(len(n)):
    n[i] = n[i]**2

print(sum(n)%10)