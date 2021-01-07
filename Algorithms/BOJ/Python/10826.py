# https://www.acmicpc.net/problem/10826
# 피보나치 수 4
import sys
n = int(sys.stdin.readline())
f = [0] * 10001
f[0] = 0
f[1] = 1
for i in range(2, 10001):
    f[i] = f[i-1] + f[i-2]
print(f[n])