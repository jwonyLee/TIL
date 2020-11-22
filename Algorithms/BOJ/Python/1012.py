# https://www.acmicpc.net/problem/1012
# 유기농 배추
import sys
sys.setrecursionlimit(10000000)

def dfs(i, j):
    if i < 0 or i >= len(grid) or \
        j < 0 or j >= len(grid[0]) or \
        grid[i][j] != 1:
        return
    
    grid[i][j] = 0
    
    # 동서남북 탐색
    dfs(i + 1, j)
    dfs(i - 1, j)
    dfs(i, j + 1)
    dfs(i, j - 1)

T = int(sys.stdin.readline())

for _ in range(T):
    m, n, k = map(int, sys.stdin.readline().split())
    grid = [[0]*m for i in range(n)]
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        grid[y][x] = 1
    
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                dfs(i, j)
                count += 1
    
    print(count)