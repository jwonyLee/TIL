# https://www.acmicpc.net/problem/2442
# 별 찍기 - 5
import sys

n = int(sys.stdin.readline())

for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    for j in range(i+1):
        print("*", end="")
    for j in range(i):
        print("*", end="")
    print()