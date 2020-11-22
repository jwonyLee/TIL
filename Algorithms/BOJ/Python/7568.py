# https://www.acmicpc.net/problem/7568
# 덩치
import sys

n = int(sys.stdin.readline())
p = []
check = [1 for _ in range(n)]

for _ in range(n):
    p.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(n):
        if i != j and p[i][0] < p[j][0] and p[i][1] < p[j][1]:
            check[i] += 1

print(" ".join(map(str, check)))