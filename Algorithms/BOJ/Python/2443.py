# https://www.acmicpc.net/problem/2443
# 별 찍기 - 6
import sys

n = int(sys.stdin.readline())
for i in range(0, n):
    print(" "*i, end="")
    print("*"*(2*n-(2*i)-1))