# https://www.acmicpc.net/problem/1926
# 그림
import sys
sys.setrecursionlimit(10000000)
n, m = map(int, sys.stdin.readline().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, sys.stdin.readline().split())))

def bfs(i, j):
    global mx
    if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] != 1:
        return
    
    # 현재 위치 방문
    grid[i][j] = 0
    mx += 1

    bfs(i+1, j)
    bfs(i-1, j)
    bfs(i, j+1)
    bfs(i, j-1)

cnt = 0
mx = 0
total = 0
if len(grid[0]) > 0:
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                mx = 0
                bfs(i, j)
                cnt += 1
                if total < mx:
                    total = mx
print(cnt)
print(total)