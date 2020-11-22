# https://www.acmicpc.net/problem/17299
# 오등큰수
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
cnt = dict()
ans = [-1 for i in range(0, n)]
s = []

for i in range(0, n):
    cnt[a[i]] = cnt.get(a[i], 0) + 1

for i in range(0, n):
    while s and cnt[a[s[-1]]] < cnt[a[i]]:
        ans[s.pop()] = a[i]
    s.append(i)
    
print(" ".join(map(str, ans)))