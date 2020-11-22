# https://www.acmicpc.net/problem/11004
# K번째 수
import sys
n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
a.sort()
print(a[k-1])