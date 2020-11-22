# https://www.acmicpc.net/problem/2440
import sys

# n =  int(sys.stdin.readline())
n = 5
for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print("*", end="")
    print()