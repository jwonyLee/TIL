# https://www.acmicpc.net/problem/1934
# 최소공배수
import sys

def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

n = int(sys.stdin.readline().strip())
for _ in range(0, n):
    a, b = map(int, sys.stdin.readline().strip().split())
    print(int(abs(a*b) / gcd(a,b)))