# https://www.acmicpc.net/problem/2178
# 미로 탐색
import sys
n, m = map(int, sys.stdin.readline().split())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
graph = []
def bfs(i, j):
    queue = [[i, j]]
    while queue:
        vi, vj = queue.pop(0)
        for x, y in zip(dx, dy):
            nx = vi + x
            ny = vj + y
            # index를 벗어난 경우
            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
            # 벽인 경우
            if graph[nx][ny] == 0: continue
            # 해당 노드를 처음 방문한 경우에만 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[vi][vj] + 1
                queue.append([nx, ny])
    return graph[n-1][m-1]
for _ in range(n):
    graph.append(list(map(int, list(sys.stdin.readline().strip()))))

print(bfs(0, 0))