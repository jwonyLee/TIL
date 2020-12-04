# https://www.acmicpc.net/problem/11724
# 연결 요소의 개수
import sys
def bfs(start_v):
    discovered = [start_v]
    queue = [start_v]
    while queue:
        x = queue.pop(0)
        if x in graph:
            for w in graph[x]:
                if w not in discovered:
                    discovered.append(w)
                    queue.append(w)
    return discovered

n, m = map(int, sys.stdin.readline().split())
graph = dict()
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    if u in graph:
        graph[u].append(v)
    else:
        graph[u] = [v]
    if v in graph:
        graph[v].append(u)
    else:
        graph[v] = [u]

total = 0
visited = []
for i in range(1, n+1):
    if i not in visited:
        visited.extend(bfs(i))
        total += 1
print(n - len(visited) + total)