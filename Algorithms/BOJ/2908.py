# https://www.acmicpc.net/problem/2908
# 상수

import sys

A, B = sys.stdin.readline().strip().split(' ')
rA = ''
rB = ''

for a in range(len(A)-1, -1, -1):
    rA += A[a]
    rB += B[a]

if int(rA) < int(rB):
    print(rB)
else:
    print(rA)