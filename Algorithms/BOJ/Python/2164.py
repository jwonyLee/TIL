# https://www.acmicpc.net/problem/2164
# 카드2
import sys, collections
n = int(sys.stdin.readline())
q = collections.deque([i for i in range(1, n+1)])
while len(q) > 1:
    q.popleft()
    q.append(q.popleft())
print(q[0])