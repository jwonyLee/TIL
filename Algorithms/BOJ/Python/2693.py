# https://www.acmicpc.net/problem/2693
# N번째 큰 수
import sys
t = int(sys.stdin.readline())
for _ in range(t):
    a = list(map(int, sys.stdin.readline().strip().split()))
    print(sorted(a, reverse=True)[2])