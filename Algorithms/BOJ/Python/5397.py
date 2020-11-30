# https://www.acmicpc.net/problem/5397
# 키로거
import sys
n = int(sys.stdin.readline())
for _ in range(n):
    L = sys.stdin.readline().strip()
    left = []
    right = []
    for s in L:
        if s == "-":
            if left:
                left.pop()
        elif s == "<":
            if left:
                right.append(left.pop())
        elif s == ">":
            if right:
                left.append(right.pop())
        else: # character
            left.append(s)
    print(''.join(left) + ''.join(right[::-1]))