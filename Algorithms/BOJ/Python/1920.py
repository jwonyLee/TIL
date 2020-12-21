# https://www.acmicpc.net/problem/1920
# 수 찾기
import sys
from collections import defaultdict
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().strip().split()))
check = defaultdict(int)
for i in a:
    check[i] = 1
for i in x:
    print(check[i])