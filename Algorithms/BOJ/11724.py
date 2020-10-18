import sys
import collections

def dfs(v, visited=[]):
    visited.append(v)

    for w in graph[v]:
        if not w in visited:
            visited = dfs(w, visited)
    return visited

graph = collections.defaultdict(list)

m, n = map(int, sys.stdin.readline().split())

for _ in range(n):
    key, value = map(int, sys.stdin.readline().split())
    graph[key].append(value)
    graph[value].append(key)

count = 0
d = []
for i in graph:
    if not i in d:
        d += dfs(i)
        count += 1
        print(d)

print(count)