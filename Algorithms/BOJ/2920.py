# https://www.acmicpc.net/problem/2920
# 음계
import sys

n = list(map(int, sys.stdin.readline().split()))

if sorted(n) == n:
    print("ascending")
elif sorted(n, reverse=True) == n:
    print("descending")
else:
    print("mixed")