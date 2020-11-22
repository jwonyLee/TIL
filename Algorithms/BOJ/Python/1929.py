# https://www.acmicpc.net/problem/1929
# 소수 구하기
import sys

def eratos(m, n):
    prime = [None for i in range(n+1)]
    check = [False for i in range(n+2)]
    pn = 0

    for i in range(2, n+1):
        if not check[i]:
            prime[pn] = i
            pn += 1

        j = i*i
        while j <= n:
            check[j] = True
            j += i
    
    prime = list(filter(lambda x: x >= m, [p for p in prime if p]))
    return prime

m, n = map(int, sys.stdin.readline().split())
prime = eratos(m, n)
for p in prime:
    print(p)