# https://www.acmicpc.net/problem/18258
# 큐 2
import sys, collections
n = int(sys.stdin.readline())
q = collections.deque()
for _ in range(n):
    op = sys.stdin.readline().strip()
    if op == "pop":
        print(q and q.popleft() or -1)
    elif op == "size":
        print(len(q))
    elif op == "empty":
        if q:
            print(0)
        else:
            print(1)
    elif op == "front":
        print(q and q[0] or -1)
    elif op == "back":
        print(q and q[-1] or -1)
    else:
        x = op.split()[-1]
        q.append(x)