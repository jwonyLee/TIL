# https://www.acmicpc.net/problem/4963
# 섬의 개수
import sys
def bfs(i, j):
    discovered = [[i, j]]
    queue = [[i, j]]
    while queue:
        vi, vj = queue.pop(0)
        for x, y in zip(dx, dy):
            nx = vi + x
            ny = vj + y
            if nx < 0 or nx >= h or ny < 0 or ny >= w or graph[nx][ny] != '1':
                continue
            if [nx, ny] not in discovered:
                discovered.append([nx, ny])
                queue.append([nx, ny])
                graph[nx][ny] = '0'
    return discovered

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    dx = [-1, 0, 1, 0, -1, -1, 1, 1]
    dy = [0, 1, 0, -1, -1, 1, 1, -1]
    graph = []
    for _ in range(h):
        graph.append(sys.stdin.readline().strip().split())
    total = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == '1':
                bfs(i, j)
                total += 1
    print(total)