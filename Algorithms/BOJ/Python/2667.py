# https://www.acmicpc.net/problem/2667
# 단지번호붙이기
import sys
n = int(sys.stdin.readline())
grid = []
nx = [1, 0, -1, 0]
ny = [0, 1, 0, -1]

def iterative_bfs(i: int, j: int):
    discovered = [[i, j]]
    queue = [[i, j]]
    while queue:
        v = queue.pop(0)
        grid[i][j] = '0'
        for (x, y) in zip(nx, ny):
            ix = v[0] + x
            iy = v[1] + y
            if ix < 0 or ix >= n or iy < 0 or iy >= n or grid[ix][iy] != "1":
                continue
            if [ix, iy] not in discovered:
                discovered.append([ix, iy])
                queue.append([ix, iy])
                grid[ix][iy] = '0'
    return len(discovered)

for _ in range(n):
    grid.append(list(sys.stdin.readline().strip()))
total = 0
cnt = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == '1':
            cnt.append(iterative_bfs(i, j))
            total += 1
cnt.sort()
print(total)
for c in cnt:
    print(c)