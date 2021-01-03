# https://www.acmicpc.net/problem/1927
# 최소 힙
import sys, heapq
h = []
for _ in range(int(sys.stdin.readline())):
    x = int(sys.stdin.readline())
    if h and x == 0:
        print(heapq.heappop(h))
    elif x == 0:
        print("0")
    else:
        heapq.heappush(h, x)