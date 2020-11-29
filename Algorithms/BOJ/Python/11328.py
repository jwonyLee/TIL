# https://www.acmicpc.net/problem/11328
# Strfry
import sys

n = int(sys.stdin.readline())
for _ in range(n):
    a, b = sys.stdin.readline().split()
    if sorted(a) == sorted(b):
        print("Possible")
    else:
        print("Impossible")