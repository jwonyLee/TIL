# https://www.acmicpc.net/problem/2231
# 분해합
import sys

n = int(sys.stdin.readline())
d = [0 for _ in range(n+1)]

for i in range(n+1):
   d[i] = i + sum(map(int, list(str(i))))

def find():
    for i in range(n+1):
        if d[i] == n:
            return i
    
    return 0

print(find())
