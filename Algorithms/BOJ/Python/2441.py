# https://www.acmicpc.net/problem/2441
# 별 찍기 - 4
import sys

n = int(sys.stdin.readline())

for i in range(n):
    for j in range(i):
        print(" ", end="")
    for j in range(n-i-1, -1, -1):
        print("*", end="")
    print()