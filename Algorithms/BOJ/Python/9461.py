# https://www.acmicpc.net/problem/9461
# 파도반 수열
import sys
p = [0]*102
p[1] = 1
p[2] = 1
p[3] = 1
for i in range(4, 102):
    p[i] = p[i-2] + p[i-3]
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    print(p[n])