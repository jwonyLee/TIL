# https://www.acmicpc.net/problem/2609
# 최대공약수와 최소공배수
import sys

a, b = map(int, sys.stdin.readline().split())

def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

g = gcd(a, b)
print(g)
print(int(g * (a / g) * (b / g)))