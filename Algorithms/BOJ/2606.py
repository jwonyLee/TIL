# https://www.acmicpc.net/problem/2606
# 바이러스

import sys
import collections

def dfs(v, discovered=[]):
    discovered.append(v)
    for w in graph[v]:
        if not w in discovered:
            discovered = dfs(w, discovered)
    return discovered

graph = collections.defaultdict(list)

c = int(sys.stdin.readline())
p = int(sys.stdin.readline())

for _ in range(p):
    k, v = map(int, sys.stdin.readline().split())
    # 양방향이기 때문에 k, v 둘 다 간선 추가해줘야 함 (매우 중요)
    graph[k].append(v)
    graph[v].append(k)

print(len(dfs(1)) - 1)