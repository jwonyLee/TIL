# https://www.acmicpc.net/problem/1764
# 듣보잡
import sys
n, m = map(int, sys.stdin.readline().strip().split())
e = set()
s = set()
for _ in range(n):
    e.add(sys.stdin.readline().strip())
for _ in range(m):
    s.add(sys.stdin.readline().strip())
es = e & s
print(len(es))
for p in sorted(es):
    print(p)