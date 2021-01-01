# https://www.acmicpc.net/problem/1303
# 전쟁 - 전투
import sys
n, m = map(int, sys.stdin.readline().strip().split())
graph = []
w = []
b = []
x = [1, 0, -1, 0]
y = [0, 1, 0, -1]
c = 0
for _ in range(m):
    graph.append(list(sys.stdin.readline().strip()))
def bfs(i, j, p):
    global c
    if i < 0 or i >= m or j < 0 or j >= n or graph[i][j] != p:
        return c
    graph[i][j] = "0"
    c += 1
    for ix, iy in zip(x, y):
        bfs(i+ix, j+iy, p)
    return c
for i in range(m):
    for j in range(n):
        if graph[i][j] == "W":
            c = 0
            w.append(bfs(i, j, "W"))
        if graph[i][j] == "B":
            c = 0
            b.append(bfs(i, j, "B"))
wn = sum([k**2 for k in w])
bn = sum([k**2 for k in b])
print(wn, bn)