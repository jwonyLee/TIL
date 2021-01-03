# https://www.acmicpc.net/problem/1676
# 팩토리얼 0의 개수
import sys
p = [0] * 501
p[0] = 1
p[1] = 1
p[2] = 2
for i in range(3, 501):
    p[i] = p[i-1] * i
n = int(sys.stdin.readline())
t = str(p[n])
cur = len(t) - 1
cnt = 0
while t[cur] == "0":
    cnt += 1
    cur -= 1
print(cnt)