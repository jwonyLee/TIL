# https://www.acmicpc.net/problem/1978
# 소수 찾기
import sys

def prime(n):
    if n < 2:
        return False

    i = 2
    while i*i <= n: 
        if n % i == 0:
            return False
        i += 1
    return True

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().strip().split()))
cnt = 0

for a in arr:
    if prime(a):
        cnt += 1

print(cnt)