# https://www.acmicpc.net/problem/2675
# 문자열 반복

import sys

T = int(sys.stdin.readline().strip())
for i in range(T):
    R, S = sys.stdin.readline().strip().split(' ')
    for j in S:
        for k in range(int(R)):
            print(j, end='')
    print()