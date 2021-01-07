# https://www.acmicpc.net/problem/2747
# 피보나치 수
import sys
f = [0] * 46
f[0] = 0
f[1] = 1
for i in range(2, 46):
    f[i] = f[i-1] + f[i-2]
n = int(sys.stdin.readline())
print(f[n])