# https://www.acmicpc.net/problem/1003
# 피보나치 함수
import sys
f = [[0, 0]] * 41
f[0] = [1, 0]
f[1] = [0, 1]
for i in range(2, 41):
    f[i] = [f[i-1][1], sum(f[i-1])]
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    print(" ".join(map(str, f[n])))