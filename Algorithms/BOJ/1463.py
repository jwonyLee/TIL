# https://www.acmicpc.net/problem/1463
# 1로 만들기
# 참고: https://www.youtube.com/watch?v=OSRD1bs9Om8

import sys

x = int(sys.stdin.readline())
d = [0 for _ in range(x+1)]

for i in range(2, x+1):
    a = 99999
    b = 99999
    c = 99999
    if i % 3 == 0:
        a = d[int(i/3)] + 1
    if i % 2 == 0:
        b = d[int(i/2)] + 1
    c = d[i -1] + 1

    d[i] = min(a, b, c)

print(d[x])