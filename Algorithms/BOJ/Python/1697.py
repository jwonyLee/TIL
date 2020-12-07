# https://www.acmicpc.net/problem/1697
# 숨바꼭질
from collections import deque
import sys
n, k = map(int, sys.stdin.readline().strip().split())
board = [-1] * 100001
board[n] = 0
queue = deque([n])
discovered = [n]
while board[k] == -1:
    v = queue.popleft()
    for nxt in [v-1, v+1, 2*v]:
        if nxt < 0 or nxt > 100000 or board[nxt] != -1: continue
        board[nxt] = board[v] + 1
        queue.append(nxt)
print(board[k])