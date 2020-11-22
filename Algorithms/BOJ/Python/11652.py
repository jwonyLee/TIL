# https://www.acmicpc.net/problem/11652
# 카드
import sys
n = int(sys.stdin.readline())
dict = {}
for _ in range(n):
    i = int(sys.stdin.readline())
    dict[i] = dict.get(i, 0) + 1
mv = max(dict.values())
mks = [k for k, v in dict.items() if v == mv]
mks.sort()
print(mks[0])