# https://www.acmicpc.net/problem/10026
# 적록색약
import sys
from collections import deque
n = int(sys.stdin.readline())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
graph = []
graphc = []
for g in range(n):
    graph.append(list(sys.stdin.readline().strip()))
    graphc.append(list(''.join(graph[g]).replace("R", "G")))
cnt = 0
cntg = 0
for i in range(n):
    for j in range(len(graph[i])):
        if graph[i][j] != '0':
            discovered = [[i, j]]
            queue = deque([[i, j]])
            c = graph[i][j]
            while queue:
                x, y = queue.popleft()
                for nx, ny in zip(dx, dy):
                    ix = nx + x
                    iy = ny + y
                    if ix < 0 or ix >= n or iy < 0 or iy >= n or graph[ix][iy] == '0' or graph[ix][iy] != c:
                        continue
                    discovered.append([ix, iy])
                    queue.append([ix, iy])
                    graph[ix][iy] = '0'
            cnt += 1
        if graphc[i][j] != '0':
            discovered = [[i, j]]
            queue = deque([[i, j]])
            c = graphc[i][j]
            while queue:
                x, y = queue.popleft()
                for nx, ny in zip(dx, dy):
                    ix = nx + x
                    iy = ny + y
                    if ix < 0 or ix >= n or iy < 0 or iy >= n or graphc[ix][iy] == '0' or graphc[ix][iy] != c:
                        continue
                    discovered.append([ix, iy])
                    queue.append([ix, iy])
                    graphc[ix][iy] = '0'
            cntg += 1
print(cnt, cntg)