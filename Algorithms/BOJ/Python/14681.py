# https://www.acmicpc.net/problem/14681
# 사분면 고르기

import sys

x = int(sys.stdin.readline().strip())
y = int(sys.stdin.readline().strip())

if x < 0: # 2, 3
    if y < 0:
        print(3)
    else:
        print(2)
else:
    if y < 0: # 1, 4
        print(4)
    else:
        print(1)