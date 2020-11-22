# https://www.acmicpc.net/problem/11726
# 2 * n 타일링
import sys 

n = int(sys.stdin.readline())
d = [0 for _ in range(n+1)]
d[0] = 1
d[1] = 1

for i in range(2, n + 1):
    d[i] = d[i-1] + d[i-2]

print(d[n] % 10007)