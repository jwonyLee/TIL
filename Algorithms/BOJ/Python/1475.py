# https://www.acmicpc.net/problem/1475
# 방 번호
import sys, math
n = sys.stdin.readline().strip()
num = [0 for _ in range(9)]

for i in n:
    if int(i) == 9:
        num[6] += 1
    else:
        num[int(i)] += 1

m = 0
for i in range(len(num)):
    if i == 6 and num[i] >= 2:
        num[i] = math.ceil(num[i]/2)
    if m < num[i]:
        m = num[i]

print(int(m))