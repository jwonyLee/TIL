# https://www.acmicpc.net/problem/1260
# DFS와 BFS
import sys
import collections

def dfs(v, discovered=[]):
    discovered.append(v)
    for w in sorted(graph[v]):
        if not w in discovered:
            discovered = dfs(w, discovered)
    return discovered

def bfs(start_v):
    discovered = [start_v]
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        for w in sorted(graph[v]):
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
    return discovered

graph = collections.defaultdict(list)

n, m, start = map(int, sys.stdin.readline().split())

for _ in range(m):
    key, value = map(int, sys.stdin.readline().split())
    graph[key].append(value)
    graph[value].append(key)

print(' '.join(map(str, dfs(start))))
print(' '.join(map(str, bfs(start))))