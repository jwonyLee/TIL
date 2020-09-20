# https://www.acmicpc.net/problem/10825
# 국영수
# https://suri78.tistory.com/109 참고
import sys
n = int(sys.stdin.readline())

c = []
for _ in range(n):
    c.append(sys.stdin.readline().split())

c.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in c:
    print(i[0])