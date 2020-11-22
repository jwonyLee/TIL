# https://www.acmicpc.net/problem/2446
# 별 찍기 - 9
import sys

n = int(sys.stdin.readline())

for i in range(2*n-1):
    if i < n:
        print(" "*i, end="")
        print("*"*(2*(n-i)-1))
    else:
        print(" " *abs(i + (n - 1) * -2), end="")
        print("*"*(2*(n-abs(i + (n - 1) * -2))-1))