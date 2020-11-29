# https://www.acmicpc.net/problem/10807
# 개수 세기
import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().strip().split()))
cnt = [0 for _ in range(201)]
v = int(sys.stdin.readline())
for a in arr:
    cnt[100+a] += 1

print(cnt[100+v])