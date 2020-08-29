# https://www.acmicpc.net/problem/9613
# GCD 합
import sys

# a, b = b, r b = 0
def gcd(a, b):
    while b != 0:
        r = a % b
        a, b = b, r
    return a

n = int(sys.stdin.readline())

for _ in range(n):
    arr = list(map(int, sys.stdin.readline().split()))
    ans = 0

    for i in range(1, len(arr)):
        for j in range(i+1, len(arr)):
            ans += gcd(arr[i], arr[j])

    print(ans)